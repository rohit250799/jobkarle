Problem:

1. Forbidden (CSRF token from POST incorrect.): /login/ -> For security reasons, CSRF tokens are rotated each time a user logs in. Any page with a form generated before a login will have an old, invalid CSRF token and need to be reloaded. This might happen if a user uses the back button after a login or if they log in a different browser tab. 
As for fixing it, there's neither a straightforward way nor a great reason to do so. If the user encounters an error in this unlikely scenario all they have to do is reload the page. So I wouldn't bother if I were you.
