# UniTryhards

Course project for "Internet Applications Design and Development" of the Department of Business Administration at the National and Kapodistrian University of Athens.

**Disclaimer:** To run the application, you will need to have Django and Git installed. Once you pull the project from our respective Repository into Visual Studio Code (VSC), you will type the following commands in the VSC Terminal to run the web application - UniTryhards. If the result shown in the screenshot below is returned, then you are good to go!

![image](https://github.com/user-attachments/assets/db644eee-58e5-451a-bc06-d2e88b91ae3c)



**1. Description of the application and its primary goals:**

Our application is named UniTryhards. First and foremost, the name is derived from two words: Uni (short for University) and Tryhards (a term used to describe someone who puts in great effort to achieve a set goal). The primary goal of the application is to offer a free service to any user—even if they are not a student—allowing them to view, download, and comment on various files (course notes, past exam papers, and further supporting material) as they see fit. Specifically, it functions as a support tool for those who choose to use it.

Additionally, the core need addressed by the application is the availability of the aforementioned documents, as well as the continuous addition of new files to the platform. It is worth noting that such documents are often absent from many university websites; consequently, some students face difficulties preparing for exams without supporting material to guide them or past exam papers to familiarize them with the potential structure of a test.

Furthermore, the application will exclusively support Greek universities and their respective departments and courses (see screenshots below). While it is accessible to anyone, it is primarily aimed at Greek students seeking additional guidance from others within this mutual aid network during their studies. Finally, we have created a Discord Server for team-studying, featuring chat rooms and live channels for those interested (see screenshots below).

![image](https://github.com/user-attachments/assets/b212d39e-2b87-485f-b04b-a7ab49e18e27)
![image](https://github.com/user-attachments/assets/60fc8f98-b515-4cb2-9fd5-14d9c4c578b5)
![image](https://github.com/user-attachments/assets/fc0f8b89-f69c-4d41-8aa6-641ce89eadc7)
![image](https://github.com/user-attachments/assets/ce740ee9-e292-4db0-b4c8-86b84180e536)
![image](https://github.com/user-attachments/assets/088aebef-6ca4-42f9-be6e-c00e86d2ca99)



**2. Description and documentation of the application's functions:**

**Function 1: User Sign Up**

- Description: The application presents the user with three mandatory fields to complete in order to create an account on the platform and gain access to all features (uploading files, commenting, downloading files). Once the initial Sign Up is complete, the user will be able to sign in via the Log In page for future visits.

- Input: The user must enter a username (pseudonyms are allowed) and a password of their choice, then confirm the password a second time. Upon clicking the "Sign Up" button, the account is created, provided the fields meet the application's requirements.

- Output: The user is redirected to the application's Home screen, where they can access all available features through the Menu or read the overview of the application and its services.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/67eb65fb-8c52-4d92-98f0-d4040dee5735)



**Function 2: User Login**

- Description: Following the completion of the Sign Up process, the user can now log in to the application whenever they wish.

- Input: The user is required to complete two fields this time. In the first, they must enter their username (unique for each user) and the password they selected during the Sign Up process. They then click the "Login" button.

- Output: The user is directed to the application's Home screen, from where they can access all the features provided in the Menu.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/60f8e7ab-8b90-4367-aee7-15396f6a1012)



**Function 3: File Upload**

- Description: Once the user is logged into the website, they will have the ability to upload files. When selecting a file, they are encouraged to provide a title and a description. Additionally, they can categorize the file by selecting from a list of specific tags (Notes, Past Exam Questions, General), and choose the specific course it belongs to, helping other users locate the file more easily.

- Input: The user selects a file from their local documents and submits it by clicking Upload.

- Output: The file is uploaded to the website and becomes visible to all users.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/00bfc83b-d821-40eb-bf3e-84ccc05a16d2)



**Function 4: View Paper and Download Paper**

- Description: At any time, users can view or download any file of interest from the website and save it to their computer.

- Input: The user selects a file from the website and clicks on it to reveal the View Paper or Download Paper buttons, then initiates the download by clicking the button if needed.

- Output: The file will now be available in the Downloads folder of the user's device.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/8529d00f-9142-40d6-8662-91e909b51764)



**Function 5: Favorite Paper and Report Paper**

- Description: Users can add any file available on the website to their personal favorites list (located in their Profile - Favourite Papers) and, of course, remove it by undoing the action. Additionally, if the content of a specific Paper is inappropriate for the application's environment, the user can Report it. Along with this action, they have the option to include a message explaining the reason for the report.

- Input: The user selects a post from the website and clicks the Favorite button (star icon).

- Output: The file is now included in the user's list of favorite posts.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/82cfdb89-a72f-4fc9-a020-79f6f8aed715)
![image](https://github.com/user-attachments/assets/17296330-22cf-4ae2-9dc8-60eee47b9e7b)
![image](https://github.com/user-attachments/assets/754d5786-fe13-4d89-ac9e-9205cf4855e1)
![image](https://github.com/user-attachments/assets/e9dc1d7a-de0c-4e82-9e14-7f90f7e76ba2)



**Function 6: File Commenting**

- Description: Users have the ability to comment on any post with a message that does not exceed 500 characters.

- Input: The user types their comment into the "Write your comment" box and clicks the Submit button to upload it to the platform.

- Output: The comment is published, allowing all users to read and interact with it.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/3bd1af9d-4fb7-4e6e-b67a-8df0b5ce617f)



**Function 7: Paper Filtering**

- Description: Filtering functions are provided for the user's convenience when searching for files within a specific course. This way, if they are looking for something specific—for example, notes—they can click the Notes button to filter the results accordingly.

- Input: The user filters the results if they are searching for a specific type of material within a given course.

- Output: The files (if any) that match the selected filter are displayed on the user's screen.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/aa108a84-ca22-4fff-a95e-7af5b976452d)
![image](https://github.com/user-attachments/assets/3aca2aec-1e15-4982-a147-eef7c2859ee0)
![image](https://github.com/user-attachments/assets/b9650ec7-33b2-4e87-85d6-806fe16150ce)
![image](https://github.com/user-attachments/assets/c9f3251d-7ba1-4598-9e26-1c4e29624ea0)



**Function 8: User Logout**

- Description: Once the user has completed their tasks within the application, they can proceed to log out.

- Input: The user clicks the Menu icon at the top left, which displays a list of options where the last one is Logout.

- Output: The user is logged out of the application and redirected to the Login screen. They must log in again to regain access to the application's features.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/6f7faaee-aaf4-4ed4-a649-cdb4d7821694)



**Function 9: User Profile Editing**

- Description: Users can edit their profile on the Profile page to change their username (unique for each person), email (unique for each user), and bio.

- Input: The user clicks the Edit Profile button.

- Output: The user is directed to a page where they can make any desired changes to the aforementioned fields.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/b39e1d18-20d5-4639-86d5-8d1c6804756d)
![image](https://github.com/user-attachments/assets/b91fb520-a4c3-4336-b8f1-df85211f07b4)



**Function 10: User Password Change**

- Description: On the Profile page, the user can replace their current password with a new one of their choice if needed.

- Input: The user clicks the Change Password button.

- Output: A form is displayed for the user to enter their new password and confirm it.

- Mock-up Screen: See the image below:

![image](https://github.com/user-attachments/assets/71c678d0-852d-4084-a206-1505578a7144)
![image](https://github.com/user-attachments/assets/c8accbe4-b9b9-496c-a02d-5d52fa64f072)



**3. Database Schema:**

![image](https://github.com/user-attachments/assets/a9b3ce0c-30fe-499f-a6b5-f8084cd42ed9)
