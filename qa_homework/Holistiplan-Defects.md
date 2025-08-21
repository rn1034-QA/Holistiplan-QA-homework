

**Defect 1: Front-end styling is not loading correctly**  
**Steps to reproduce:**   
(1) Run `docker-compose...`,   
(2) Navigate to `localhost:8000`.  
**Expected result:** The website should have proper styling.  
**Actual result:** The website styling is broken, appearing as raw HTML. Received a 404 in the console for both the CSS and JS files  
**Severity: Cosmetic**

**Defect 2: Double slash in URL path results in 404 error**  
**Steps to Reproduce:**
1. Navigate to `http://localhost:8000/about//test` in your browser.  
2. Observe the 404 "Page Not Found" error.
**Expected Behavior:** The page should either load the correct content for `/about/test` or redirect the user to a valid page.  
**Actual Behavior:** The server returns a 404 error page.

**Defect 3: Claim My Rewards button disabled after rewards are available**  
**Steps to Reproduce:**
1. Access the homepage at [http://localhost:8000](http://localhost:8000)  
2. Observe the “claim my rewards” button is initially disabled.  
3. Click the \+5 or \+15 for earned bonus points to add a reward.  
4. Observe the rewards total and the state of the “Claim my rewards” button.
**Expected Behavior:** The “Claim my Rewards” button should become enabled after a reward has been added.  
**Severity: Critical**

**Defect 4: Incorrect point deduction for rewards**  
 **Steps to Reproduce:** 
1. Navigate to the application homepage at [http://localhost:8000/](http://localhost:8000/)  
2. Click on the \+5 text until you have 10 points  
3. Local the reward option “Potion of Endless Coffee 2.25pts”  
4. Make note of your current point balance  
5. Click the “Redeem this Reward” button/text.  
6. Observe your new balance 
**Expected Behavior:** The point balance should be reduced by exactly 2.25. The new balance should be 2.75 points.  
Actual Results: The application deducted 4.75 points from the balance. The new balance is 5.25  
**Severity: Major**

**Defect 5: Forfeit points and claim rewards functionality is inconsistent and buggy**  
**Summary**: Performing a series of actions- redeeming rewards, then forfeiting points, and then clicking “claim my rewards” leads to an unpredictable and incorrect state where points, redeemed points, and button states are inconsistent.  
**Steps to Reproduce:** 
1. Access the homepage at [http://localhost:8000](http://localhost:8000)  
2. Ensure “points remaining” and “Points Redeemed” are both at zero  
3. Click the \+5 button twice. The “points remaining” total should now be 10\.  
4. Click the “redeem this reward” button for a 1.50 pts item.  
   1. Note: The system incorrectly updates “POints Redeemed” to 4.75 and “Points Remaining” to 5.75 (This is the previously documented bug)  
5. Click the "Forfeit all Points” button  
6. Observe the updated UI. POints redeemed is 4.75 and Points Remaining is 0\.  
7. Click the “Claim my Rewards” button  
8. Observe the updated UI. “Points Redeemed” is 0 and “Points Remaining” is 2\.
**Expected Results**:   
After step 3 the “Points Remaining” should be 8.50 and the “Points Redeemed” should be 1.50.  
After step 4, “Points Remaining” should be 0, and “Points Redeemed” should logically remain at 1.50. The button state for "Forfeit all Points” should not change unexpectedly.  
After step 6, the “Points Redeemed” should be reset to 0 and the claimed points should be added to the main points balance, or the button should do nothing as there are no new rewards to claim. The UI should remain consistent.  
**Actual Results:**   
After step 3, the “Points Remaining” should be 4.75 and the “Points Redeemed” should be 5.75.  
 After step 4, “Points Remaining” is 0, and “Points Redeemed” is 4.25, and the “Forfit all Points” button disappears.   
After step 6, the page refreshes and the “Points redeemed” is 0, “Points Remaining” is 2, and the “Forfit all POints” reappears. The values are completely reset and incorrect.  
**Severity: Major**

**Defect 6: About Page Broken- 404**  
**Summary:**  
When navigating to the About page from the side bar you are taken to a page that provides a 404 error message.  
**Steps to Reproduce**:
1. Access the homepage at [http://localhost:8000](http://localhost:8000)  
2. Click on the About text in the top navigation section  
3. Observe the page takes you to 

**Defect 7: Usability/Ui bug**  
**Summary:**  
The application allows a user to click on a reward and receive it even if they do not have sufficient points, resulting in their points balance going into a negative value.  
**Steps to Reproduce**:
1. Access the homepage at [http://localhost:8000](http://localhost:8000)  
2. Ensure “points remaining” and “Points Redeemed” are both at zero  
3. Click the \+5 button twice. The “points remaining” total should now be 10\.  
4. Click the “redeem this reward” button for a 1.50 pts item.  
5. Locate a reward that costs more than your current balance (Scroll of Infinite WiFi 3.75pts)  
6. Observe the “Redeem this Reward” on other items are not grayed out and is still clickable  
7. Click the “redeem this Reward: button.  
8. Observe the points balance is negative.
**Expected Results:** The “Redeem this Reward” button for items a user cannot afford should be grayed out (or disabled) and unclickable. Clicking it should trigger a message “You don’t have enough points”. The user points balance should remain unchanged.  
**Actual Results**: THe “redeem this Reward” button is clickable even when the user cannot afford the item. Clicking it results in the points balance going into a negative value. The “Claim my Rewards” is grayed out and the user must unclick some of the rewards until the points move out of the negative value. This is a poor user experience.   
**Severity: Cosmetic/Enhancement**

**Defect 8: Login page broken by SQL injection**
**Summary:** The login page is vulnerable to SQL injection, which causes the page to break and display a black screen when a specific payload is used. 
**Steps to reproduce:** 
1. Navigate to the login page.   
2. In the username or password field, enter the SQL injection payload ' OR 1=1 \--   
3. Click the Log In button.
**Expected Result:** The login attempt should fail, and an error message (e.g., "Invalid username or password") should be displayed. The page should remain functional. 
**Actual result:** The page displays a black screen or is otherwise unresponsive. 
**Severity: Critical**

**Defect 9: Missing success message after re-sending verification**  
**Description**: After a user clicks the "re-send verification" button, no success message appears, leaving the user unsure if the action was successful.  
**Steps to reproduce:**  
(1) Log in to your account.  
(2) Navigate to My Profile.  
(3) Click the Re-send Verification button.  
**Expected result:** A success message should appear, confirming that the verification email has been resent (e.g., "Verification email resent successfully\!").  
**Actual result**: No message appears.  
**Severity: Minor**

**Defect 10: Duplicate email signup allowed**
**Description:** The system allows a user to sign up with an email address that is already in use, without any validation or error message. 
**Steps to reproduce:** 
1. Go to the sign-up page.   
2. Enter an email address that is already registered in the system (e.g., `someone@holistiplan.com`).   
3. Complete the rest of the sign-up form and submit. 
**Expected result:** The system should prevent the sign-up and display an error message stating that the email is already in use. 
**Actual result:** The sign-up process appears to be successfully on the front end when creating a new user account with a duplicate email address. However an email is sent to the user letting them know an account already exists. 
**Severity: Minor**
