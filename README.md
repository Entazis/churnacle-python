_Started implementing the churnacle project in Python to use neural networks later on._
_This was left in half. -> TensorFlow for R was realeased this year. -> Implemented churnacle with neural nets in R (churnacle-r)._

### Churnacle project description: ###
The CodeBerry Programming School wanted to know what users should we call, so they didn't churn.
I've created the data preparing, machine learning model training codes in R studio on an AWS server. I also experimented a little bit with neural networks. 
In the end, the output was a list of email addresses of the users who were predicted to churn. It was a lot better than random guessing (2/3 of the predicted users churned for real) but it needed a far more data for the training that the company hadn't got.
I've also created a program in Node.js that sends email to the predicted users for churn through Intercom.
