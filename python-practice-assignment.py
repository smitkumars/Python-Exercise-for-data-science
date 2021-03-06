#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 - Python Basics Practice
# 
# *This assignment is a part of the course ["Data Analysis with Python: Zero to Pandas"](https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas)*
# 
# In this assignment, you'll get to practice some of the concepts and skills covered in the following notebooks:
# 
# 1. [First Steps with Python and Jupyter](https://jovian.ml/aakashns/first-steps-with-python)
# 2. [A Quick Tour of Variables and Data Types](https://jovian.ml/aakashns/python-variables-and-data-types)
# 3. [Branching using Conditional Statements and Loops](https://jovian.ml/aakashns/python-branching-and-loops)
# 
# As you go through this notebook, you will find a **???** in certain places. To complete this assignment, you must replace all the **???** with appropriate values, expressions or statements to ensure that the notebook runs properly end-to-end. 
# 
# Some things to keep in mind:
# 
# * Make sure to run all the code cells, otherwise you may get errors like `NameError` for undefined variables.
# * Do not change variable names, delete cells or disturb other existing code. It may cause problems during evaluation.
# * In some cases, you may need to add some code cells or new statements before or after the line of code containing the **???**. 
# * Since you'll be using a temporary online service for code execution, save your work by running `jovian.commit` at regular intervals.
# * Questions marked **(Optional)** will not be considered for evaluation, and can be skipped. They are for your learning.
# 
# You can make submissions on this page: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-1-python-basics-practice
# 
# If you are stuck, you can ask for help on the community forum: https://jovian.ml/forum/t/assignment-1-python-practice/7761 . You can get help with errors or ask for hints, but **please don't ask for or share the full working answer code** on the forum.
# 
# 
# ## How to run the code and save your work
# 
# The recommended way to run this notebook is to click the "Run" button at the top of this page, and select "Run on Binder". This will run the notebook on [mybinder.org](https://mybinder.org), a free online service for running Jupyter notebooks. 
# 
# Before staring the assignment, let's save a snapshot of the assignment to your Jovian.ml profile, so that you can access it later, and continue your work.

# In[4]:


# Install the library
get_ipython().system('pip install jovian --upgrade --quiet')


# In[5]:


# Import it
import jovian


# In[6]:


project_name='python-practice-assignment'


# In[7]:


# Capture and upload a snapshot
jovian.commit(project=project_name, privacy='secret', evironment=None)


# You'll be asked to provide an API Key, to securely upload the notebook to your Jovian.ml account. You can get the API key from your Jovian.ml profile page after logging in / signing up. See the docs for details: https://jovian.ml/docs/user-guide/upload.html . The privacy of your assignment notebook is set to *Secret*, so that you can the evlauators can access it, but it will not shown on your public profile to other users.

# ## Problem 1 - Variables and Data Types
# 
# **Q: Assign your name to the variable `name`.**

# In[9]:


name = 'Smitkumar Suryawanshi'


# **Q: Assign your age (real or fake) to the variable `age`.**

# In[6]:


age = 29


# **Q: Assign a boolean value to the variable `has_android_phone`.**

# In[7]:


has_android_phone = True


# You can check the values of these variables by running the next cell.

# In[8]:


name, age, has_android_phone


# **Q: Create a dictionary `person` with keys `"Name"`, `"Age"`, `"HasAndroidPhone"` and values using the variables defined above.**

# In[9]:


person = {'Name':'Smitkumar Suryawanshi','Age':29,'HasAndroidPhone':True}


# Let's use the `person` dictionary to print a nice message.

# In[10]:


print("{} is aged {}, and owns an {}.".format(
    person["Name"], 
    person["Age"], 
    "Android phone" if person["HasAndroidPhone"] else "iPhone"
))


# **Q (Optional): Use a `for` loop to display the `type` of each value stored against each key in `person`.**
# 
# Here's the expected output for the key `"Name"`: 
# 
# ```
# The key "Name" has the value "Derek" of the type "<class 'str'>"
# ```

# In[16]:


# this is optional
person["Name"]="Derek"
for key in person:
    print(key)
    
print(person) 


# Now that you've solved one problem, it would be a good idea to record a snapshot of your notebook.

# In[11]:


jovian.commit(project=project_name,environment=None)


# ## Problem 2 - Working with Lists
# 
# **Q: Create a list containing the following 3 elements:**
# 
# * your favorite color
# * the number of pets you have
# * a boolean value describing whether you have previous programming experience
# 

# In[13]:


my_list = ['Blue',2,True]


# Let's see what the list looks like:

# In[14]:


my_list


# **Q: Complete the following `print` and `if` statements by accessing the appropriate elements from `my_list`.**
# 
# *Hint*: Use the list indexing notation `[]`.

# In[35]:


print('My favorite color is', my_list[0])


# In[36]:


print('I have {} pet(s).'.format(my_list[1]))


# In[37]:


if my_list[2] is True:
    print("I have previous programming experience")
else:
    print("I do not have previous programming experience")


# **Q: Add your favorite single digit number to the end of the list using the appropriate list method.**

# In[38]:


my_list.append('1')


# Let's see if the number shows up in the list.

# In[39]:


my_list


# **Q: Remove the first element of the list, using the appropriate list method.**
# 
# *Hint*: Check out methods of list here: https://www.w3schools.com/python/python_ref_list.asp

# In[40]:


my_list.remove('Blue')


# In[3]:


my_list


# **Q: Complete the `print` statement below to display the number of elements in `my_list`.**

# In[15]:


print("The list has {} elements.".format(my_list))


# Well done, you're making good progress! Save your work before continuing

# In[16]:


jovian.commit(project=project_name,environment=None)


# ## Problem 3 - Conditions and loops
# 
# **Q: Calculate and display the sum of all the numbers divisible by 7 between 18 and 534 i.e. `21+28+35+...+525+532`**.
# 
# *Hint*: One way to do this is to loop over a `range` using `for` and use an `if` statement inside it.

# In[44]:


# store the final answer in this variable
sum_of_numbers = 0


for i in range (18,534) :
    if(i%7==0):
        sum_of_numbers +=i
        
          
print(sum_of_numbers)
# perform the calculation here


# In[45]:


print('The sum of all the numbers divisible by 7 between 18 and 534 is', sum_of_numbers)


# If you are not able to figure out the solution to this problem, you can ask for hints on the community forum: https://jovian.ml/forum/t/assignment-1-python-practice/7761 . Remember to save your work before moving forward.

# In[46]:


jovian.commit(project=project_name,environment=None)


# ## Problem 4 - Flying to the Bahamas
# 
# **Q: A travel company wants to fly a plane to the Bahamas. Flying the plane costs 5000 dollars. So far, 29 people have signed up for the trip. If the company charges 200 dollars per ticket, what is the profit made by the company?**
# 
# Fill in values or arithmetic expressions for the variables below.

# In[49]:


cost_of_flying_plane = 5000


# In[50]:


number_of_passengers = 29


# In[51]:


price_of_ticket = 200


# In[52]:


profit = (price_of_ticket * number_of_passengers)-cost_of_flying_plane


# In[53]:


print('The company makes of a profit of {} dollars'.format(profit))


# **Q (Optional): Out of the 29 people who took the flight, only 12 buy tickets to return from the Bahamas on the same plane. If the flying the plane back also costs 5000 dollars, and does the company make an overall profit or loss? The company charges the same fee of 200 dollars per ticket for the return flight.**
# 
# Use an `if` statement to display the result.

# In[57]:


# this is optional
number_of_passengers=12
price_of_ticket = 200
cost_of_flying_plane = 5000

profit = (price_of_ticket * number_of_passengers)-cost_of_flying_plane
print(profit)


# In[59]:


# this is optional
if profit==800:
    print("The company makes an overall profit of {} dollars".format(profit))
else:
    print("The company makes an overall loss of {} dollars".format(profit))


# Great work so far! Want to take a break? Remember to save and upload your notebook to record your progress.

# In[60]:


jovian.commit(project=project_name,environment=None)


# ## Problem 5 - Twitter Sentiment Analysis
# 
# Are your ready to perform some *Data Analysis with Python*? In this problem, we'll analyze some fictional tweets and find out whether the overall sentiment of Twitter users is happy or sad. This is a simplified version of an important real world problem called *sentiment analysis*.
# 
# Before we begin, we need a list of tweets to analyze. We're picking a small number of tweets here, but the exact same analysis can also be done for thousands, or even millions of tweets. The collection of data that we perform analysis on is often called a *dataset*.

# In[61]:


tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]


# Let's begin by answering a very simple but important question about our dataset.
# 
# **Q: How many tweets does the dataset contain?**

# In[67]:


number_of_tweets = len(tweets)
print(number_of_tweets)


# Let's create two lists of words: `happy_words` and `sad_words`. We will use these to check if a tweet is happy or sad.

# In[68]:


happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']


# In[69]:


sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']


# To identify whether a tweet is happy, we can simply check if contains any of the words from `happy_words`. Here's an example:

# In[70]:


sample_tweet = tweets[0]


# In[71]:


sample_tweet


# In[79]:


is_tweet_happy = False

# Get a word from happy_words
for word in happy_words:
    # Check if the tweet contains the word
    if word in sample_tweet:
        # Word found! Mark the tweet as happy
        is_tweet_happy = True


# Do you understand what we're doing above? 
# 
# > For each word in the list of happy words, we check if is a part of the selected tweet. If the word is indded a part of the tweet, we set the variable `is_tweet_happy` to `True`. 

# In[80]:


is_tweet_happy


# **Q: Determine the number of tweets in the dataset that can be classified as happy.**
# 
# *Hint*: You'll need to use a loop inside another loop to do this. Use the code from the example shown above.

# In[102]:


# store the final answer in this variable
number_of_happy_tweets = 0

# perform the calculations here
is_tweet_happy = False

# Get a word from happy_words
number_of_happy_tweets = 0

for i in happy_words:
    for j in tweets:
        if i in j:
            number_of_happy_tweets +=1  
number_of_happy_tweets             


# In[88]:


print("Number of happy tweets:", number_of_happy_tweets)


# If you are not able to figure out the solution to this problem, you can ask for hints on the community forum: https://jovian.ml/forum/t/assignment-1-python-practice/7761 . Also try adding `print` statements inside your loops to inspect variables and make sure your logic is correct.

# **Q: What fraction of the total number of tweets are happy?**
# 
# For example, if 2 out of 10 tweets are happy, then the answer is `2/10` i.e. `0.2`.

# In[104]:


happy_fraction = 6/8


# In[105]:


print("The fraction of happy tweets is:", happy_fraction)


# To identify whether a tweet is sad, we can simply check if contains any of the words from `sad_words`.
# 
# **Q: Determine the number of tweets in the dataset that can be classified as sad.**

# In[103]:


# store the final answer in this variable
number_of_sad_tweets = 0

# perform the calculations here
for i in sad_words:
    for j in tweets:
        if i in j:
            number_of_sad_tweets +=1 
number_of_sad_tweets


# In[106]:


print("Number of sad tweets:", number_of_sad_tweets)


# **Q: What fraction of the total number of tweets are sad?**

# In[107]:


sad_fraction = 2/8


# In[108]:


print("The fraction of sad tweets is:", sad_fraction)


# The rest of this problem is optional. Let's save your work before continuing.

# In[109]:


jovian.commit(project=project_name,environment=None)


# Great work, even with some basic analysis, we already know a lot about the sentiment of the tweets given to us. Let us now define a metric called "sentiment score", to summarize the overall sentiment of the tweets.
# 
# **Q (Optional): Calculate the sentiment score, which is defined as the difference betweek the fraction of happy tweets and the fraction of sad tweets.**

# In[110]:


sentiment_score = happy_fraction - sad_fraction


# In[111]:


print("The sentiment score for the given tweets is", sentiment_score)


# In a real world scenario, we could calculate & record the sentiment score for all the tweets sent out every day. This information can be used to plot a graph and study the trends in the changing sentiment of the world. The following graph was creating using the Python data visualization library `matplotlib`, which we'll cover later in the course.
# 
# <img src="https://i.imgur.com/6CCIwCb.png" style="width:400px">
# 
# What does the sentiment score represent? Based on the value of the sentiment score, can you identify if the overall sentiment of the dataset is happy or sad?
# 
# **Q (Optional): Display whether the overall sentiment of the given dataset of tweets is happy or sad, using the sentiment score.**

# In[112]:


if sentiment_score>0.3:
    print("The overall sentiment is happy")
else:
    print("The overall sentiment is sad")


# Finally, it's also important to track how many tweets are neutral i.e. neither happy nor sad. If a large fraction of tweets are marked neutral, maybe we need to improve our lists of happy and sad words. 
# 
# **Q (Optional): What is the fraction of tweets that are neutral i.e. neither happy nor sad.**

# In[113]:


# store the final answer in this variable
number_of_neutral_tweets = 0

# perform the calculation here


# In[114]:


neutral_fraction = 0


# In[115]:


print('The fraction of neutral tweets is', neutral_fraction)


# Ponder upon these questions and try some experiments to hone your skills further:
# 
# * What are the limitations of our approach? When will it go wrong or give incorrect results?
# * How can we improve our approach to address the limitations?
# * What are some other questions you would like to ask, given a list of tweets?
# * Try collecting some real tweets from your Twitter timeline and repeat this analysis. Do the results make sense?
# 
# **IMPORTANT NOTE**: If you want to try out these experiments, please create a new notebook using the "New Notebook" button on your Jovian.ml profile, to avoid making unintended changes to your assignment submission notebook.

# ## Submission 
# 
# Congratulations on making it this far! You've reached the end of this assignment, and you just completed your first data analysis problem. It's time to record one final version of your notebook for submission.
# 
# Make a submission here by filling the submission form: https://jovian.ml/learn/data-analysis-with-python-zero-to-pandas/assignment/assignment-1-python-basics-practice

# In[116]:


jovian.commit(project=project_name,environment=None)


# In[ ]:




