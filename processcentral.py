
def processCentral(user):
    import pandas as pd
    from datetime import datetime

    user_next = pd.DataFrame()

    if ('authentication' in user.index):
        email_address = user['authentication']['email_address']
        if ('slack_user_id' in user['authentication']):
            slack_user_id = True #user['authentication']['slack_user_id']
        else:
            slack_user_id = False
        if ('facebook_user_id' in user['authentication']):
            facebook_user_id = True #user['authentication']['facebook_user_id']
        else:
            facebook_user_id = False
        if ('google_user_id' in user['authentication']):
            google_user_id = True #user['authentication']['google_user_id']
        else:
            google_user_id = False
    if ('locale' in user.index):
        locale = user['locale']['fullLocaleCode']
    if ('address' in user.index):
        pass
    if (('campaign' in user.index) and (user['campaign'] is dict)):
        if ('utm_source' in user['campaign']):
            utm_source = user['campaign']['utm_source']
        if ('utm_medium' in user['campaign']):
            utm_medium = user['campaign']['utm_medium']
        if ('utm_campaign' in user['campaign']):
            utm_campaign = user['campaign']['utm_campaign']
    if ('curriculumPermissions' in user.index):
        if('internal' in user['curriculumPermissions']):
            trial_projects = user['curriculumPermissions']['internal']['trialProjects']
            paid_projects = user['curriculumPermissions']['internal']['paidProjects']
            free_materials = user['curriculumPermissions']['internal']['freeMaterials']
            cross_deals = user['curriculumPermissions']['crossDeals']
            promotions = user['curriculumPermissions']['promotions']
    if ('learning' in user.index):
        pass
    if ('codes' in user.index):
        if('coupon' in user['codes']):
            coupon = user['codes']['coupon']
    if ('oldSubscriptions' in user.index):
        old_subscriptions = user['oldSubscriptions']
    if ('personal_data' in user.index):
        pass
    if ('subscription2' in user.index):
        subscription2 = user['subscription2']

    if 'slack_user_id' not in locals():
        slack_user_id = None
    if 'facebook_user_id' not in locals():
        facebook_user_id = None
    if 'google_user_id' not in locals():
        google_user_id = None
    if 'free_materials' not in locals():
        free_materials = None
    if 'coupon' not in locals():
        coupon = None
    if 'utm_source' not in locals():
        utm_source = None
    if 'utm_medium' not in locals():
        utm_medium = None
    if 'utm_campaign' not in locals():
        utm_campaign = None

    paid_acc = 0
    num = 0
    old_subscriptions_cnt = len(old_subscriptions)

    #Loop over oldSubscriptions
    for sub_cnt, oldsubscription in enumerate(old_subscriptions):

        #Keep only the paid subscriptions
        if (('plan' in oldsubscription) and ('type' in oldsubscription['plan']) and (oldsubscription['plan']['type'] == 'paid')):

            transactions = oldsubscription['transactions']
            transactions_sum = len(transactions)

            internal_id = oldsubscription['plan']['internalId']
            period = oldsubscription['plan']['billingDetails']['periodInDays']
            price = oldsubscription['plan']['amount']['gross']

            for trans_cnt, transaction in enumerate(transactions):
                num += 1
                handler = transaction['handler']['processorName']
                paid = transaction['transaction']['amount']
                paid_acc += paid
                currency = transaction['transaction']['currency']['ISO3']
                start = transaction['transaction']['fulfillmentDateTime']

                if (trans_cnt < transactions_sum - 1):
                    paid_next = "yes"
                else:
                    paid_next = "no"

                end = start + (period*24*60*60)

                # 10-days tolerance
                if (datetime.now() < datetime.fromtimestamp(end + (10 * 24 * 60 * 60))):
                    paid_next = "unknown"

                user_sub1 = {"email_address": [email_address], "period": [num], "start": [start], "end": [end], "paid_next": [paid_next],
                             "handler": [handler],
                             "internal_id": [internal_id], "price": [price], "paid_acc": [paid_acc], "currency": [currency],
                             "locale": [locale], "slack": [slack_user_id], "facebook": [facebook_user_id], "google": [google_user_id],
                             "free_materials": [free_materials], "coupon": [coupon],
                             "utm_source": [utm_source], "utm_medium": [utm_medium], "utm_campaign": [utm_campaign]}
                entry = pd.DataFrame(user_sub1)
                user_next = user_next.append(entry)

    if((subscription2['isActive'] == True) and (subscription2['plan']['type'] == 'paid') and (len(subscription2['transactions']) > 0)):
        transactions2 = subscription2['transactions']
        transactions2_sum = len(transactions2)
        for trans_cnt2, transaction2 in enumerate(transactions2):
            num += 1

            internal_id2 = subscription2['plan']['internalId']
            period2 = subscription2['plan']['billingDetails']['periodInDays']
            price2 = subscription2['plan']['amount']['gross']
            handler2 = transaction2['handler']['processorName']
            paid2 = transaction2['transaction']['amount']
            paid_acc += paid2
            currency2 = transaction2['transaction']['currency']['ISO3']
            start2 = transaction2['transaction']['fulfillmentDateTime']
            end2 = start2 + (period2*24*60*60)

            if(trans_cnt2 < transactions2_sum-1):
                paid_next2 = "yes"
            else:
                paid_next2 = "unknown"

            # 10-days tolerance
            if (datetime.now() < datetime.fromtimestamp(end2 + (10 * 24 * 60 * 60))):
                paid_next2 = "unknown"

            user_sub2 = {"email_address": [email_address], "period": [num], "start": [start2], "end": [end2],
                         "paid_next": [paid_next2], "handler": [handler2],
                         "internal_id": [internal_id2], "price": [price2], "paid_acc": [paid_acc], "currency": [currency2],
                         "locale": [locale], "slack": [slack_user_id], "facebook": [facebook_user_id], "google": [google_user_id],
                         "free_materials": [free_materials], "coupon": [coupon],
                         "utm_source": [utm_source], "utm_medium": [utm_medium], "utm_campaign": [utm_campaign]}
            entry2 = pd.DataFrame(user_sub2)
            user_next = user_next.append(entry2)

    return user_next