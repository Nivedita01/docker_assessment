"""for maintainability, I have listed out test cases by page name, as per the severity of the test case"""

testCases = [
    " [severity,"
    " page,"
    " description,"
    " reason to choose]"

    ['major',
     'Home Page',
     'enters a keyword into the search bar and clicks on the last page of search results',
     'REASON: clicking on next page to find desired result is a basic requirement, sometimes desired results end up on'
     ' the last page too.'],

    ['major',
     'Search Page',
     'validating the search text from main page of the screen',
     'REASON: user usually wants to search from the main page instead of logging in and searching for something'],

    ['not a bug',
     'Forgot Page',
     'if no email address is entered for resetting password, the page shows appropriate message',
     'REASON: basic check to find out if reset button throws any error without entering email id'],

    ['not a bug',
     'Forgot Page',
     'if title of Landing page of Forgot Password page is as intended',
     'REASON: basic check to find out if clicking on forgot password link has ended up on forgot password page or not'],

    ['not a bug',
     'Home Page',
     'validating session management after user logs out, by clicking the back button on browser',
     'REASON: security check to see if user details can be accessed after he logs out of the system'],

    ['not a bug',
     'Sign In Page',
     'testing if a valid user can enter the system, by providing right credentials',
     'REASON: basic check to verify right user'],

    ['not a bug',
     'Sign In Page',
     'testing if an invalid user is prompted an error message when trying to login',
     'REASON: basic check to verify invalid user'],

    ['not a bug',
     'Sign Up Page',
     'verify if copying of password can be performed or not',
     'REASON: security check to see if entered password can be copied and pasted into another field']
]