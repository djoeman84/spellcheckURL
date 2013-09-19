spellcheckURL
=============

Simple Python helper to check spelling of webpages

Usage:
  
```unix
python ./spellcheckURL.py [check-type] [url] [args]
```

*check-type:* specifies the method used to select elements to be spell checked, the possible types are:
* all (check all elements in DOM)
* tag (check all elements by tag types provided in args)
* class (check all elements by class names provided in args)

*url:* full url path of target html page

*args:* arguments specifying class or tag names to be checked
