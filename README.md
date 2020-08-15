# WebCrawlin101
 A tutorial on Crawling the Web and Scraping off the Useful bits - without actually doing anything

## What is Web Crawling and Web Scraping? Are they really different?

### Web Crawling

Web Crawling is the process of going through the World Wide Web systematically and indexing it. 

Of course, not a human directly; that would be rather inefficient... We're talking about an automated bot called a Spider (or Spiderbot) that intelligently (or stupidly, depending on how you see it) goes through the entire web. ([Paraphrased from Wikipedia](https://en.wikipedia.org/wiki/Web_crawler))

The parts that you can and can't Google, all of them are visible to these nifty guys... 

They're generally used to keep stock of what's on there and where the pages rank in popularity. 
But they're capable of doing literally anything that we tell them to do with the data they gather. 

Google, or like any other search engine, are examples of web crawlers.

### Web Scraping

Web scraping is the process of getting data from the web and storing it for various uses.

A Web Scraper is similar to a Web Crawler, except that it involves reading Human Readable text and trying to get a machine to do the same. It's a lot more time consuming to write, since you would have to manually look through the various HTML tags and such, but the whole process is easier overall, since you would only have to imagine how you would be doing the same things yourself.

On the other hand, a web crawler requires you to be able to know exactly what you want to do without having a very clear visual idea of how things are, but are a lot easier to code once you have the overall idea in mind.


### What's the difference??? I'm confused dude!

In the end, Web Crawling is something that computers can do much better since Humans aren't very good at navigating webpages without visual information. On the other hand, Web Scraping is a task that humans could do pretty well, but slowly. That task can be automated using a computer to make it much faster and save the user's time. 

We're definitely going to be making a Web Scraper here, and not a Web Crawler as of now, although that'll also be done eventually.

In the end, Web Crawlers and Web Scrapers aren't really all that different if you look at what they're doing.
Since they're like a niche within a niche, it is sometimes hard to see the exact difference between them, so let's get started!


## Enter Selenium!

Selenium was originally intended to be used for testing web pages for web development. 

However, people realised that it could also be used for Web Scraping since it offers full-fledged control over all the features of a browser, down to opening new tabs and creating new bookmarks!

We will be making use of Selenium in Python here, but do keep in mind that it has a Java version as well, which can be used for the same purposes, if you're more into Java.

