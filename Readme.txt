Impressions of this term project 
and lessons learnt in designing the 
software architecture: We think the 
term project was really interesting 
and exposed us to real 
implementation of the architectures
 we draw and adapt the necessary 
changes as we go. The peer reviews 
gave us a taste of working in an agile environment and we tried our best to include anything that we thought was feasible for us. 
We learned that the development of 
a software starts with a customer 
need. As we go through the 
implementation, we need to make a 
clear choice about our target users 
and their needs, think about what 
methodology, patterns and 
architectures to use, so they 
match the requirements of our 
idea’s implementation, should 
account and leave space future 
errors and extensions, i.e. make 
it as flexible as possible. Though 
while designing, we don’t have to 
focus on the development phase, 
and just be concerned with the 
architecture. We realized that its 
difficult to match the exact same 
architecture and there will be 
difficulties and we will need to 
make changes according to the user 
needs and requirements later as we 
go.

Final tally of patterns used, 
vulnerabilities discovered:

Initially, we wanted to use a
 framework and externals APIs to 
create a small-scale Yelp for 
Healthcare review application.  
We wanted to have three types of 
accounts, Company, Customer, and 
Admin profiles. We planned to use 
an MVC approach to update the 
profiles and create reviews. 
 As time went on, we saw some 
difficulties in the project but 
still wanted to deliver a full 
application.  Therefore we had to 
cut some features down such as the 
admin profile and focused on the 
two major profiles (UserProfile 
and CustomerProfile). Originally 
we had planned on using Heroku and
 MySQL but this proved difficult 
in the limited timeframe.  We kept 
the original implementation of 
the django database. Overall, the 
largest switch was from an MVC 
model to the MVT pattern as that 
is what Django mainly uses. Rest 
of our pattern pretty much 
remained the same, and so did 
the database backend. 
