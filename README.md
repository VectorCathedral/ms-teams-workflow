# 🚀 Send Notes to Students via Microsoft Teams

This project automates sending personalized Teams messages 📩 to students with their study notes 📖. It combines Python 🐍, Microsoft Teams Workflows ⚡, and Excel/CSV files 📊 to deliver notes seamlessly.

🛠️ Setting Up Your Microsoft Teams Workflow

Before running the Python script, you’ll need to create a custom workflow in Microsoft Teams to handle incoming messages. Here’s how:

### Open Microsoft Teams 💬
## On the left pane, click Apps ➕ and search for Workflows. Add it.
<img width="1551" height="812" alt="image" src="https://github.com/user-attachments/assets/37657e13-e3af-4528-abf4-16265b901be8" />


### Create a New Flow 🌊

Open Workflows

In the top right, click New Flow

<img width="1588" height="848" alt="image" src="https://github.com/user-attachments/assets/33e89f04-1510-45dc-9749-d1fb36b3f24e" />


### Then select Create from blank

<img width="1590" height="836" alt="image" src="https://github.com/user-attachments/assets/63d929fa-dcd7-4b00-a893-8d63e1cf60d0" />


### Name Your Flow ✍️
#### Hover over the Untitled Flow text box (top-left) and give your flow a name.

## Add a Trigger 🎯

### Search for webhook and select When a Teams webhook is received

<img width="1576" height="844" alt="image" src="https://github.com/user-attachments/assets/c8622563-7b14-4c3b-92b5-722a2fa48254" />


### Leave "Who can trigger the flow" as default Anyone (the whole program works fine like this).

### Compose Step 📝

#### Add a Data Operation → Compose step
Set Inputs to:

```bash
 @triggerBody()
```

## ⚠️ Pro-tip: Type it in manually, copy it, and paste it back. For some reason, this ensures Teams recognizes it.

### Parse JSON Step 🔍

#### Add a Data Operation → Parse JSON step

Once again Set Content to :
```bash
@triggerBody()
```

### * Design your Schema and paste it in the box:

```json
{
  "type": "object",
  "properties": {
    "studnum": { "type": "string" },
    "message": { "type": "string" },
    "url": { "type": "string" }
  }
}
```
### ✅ At this point your workflow should look like the below.

 <img width="1511" height="806" alt="image" src="https://github.com/user-attachments/assets/f01dcb62-e668-47e5-8740-a63461298c74" />


### Post Message Step 💌

#### Add Post message in a chat or channel

## Configure as follows:

* Post as: Flow Bot

* Post in: Chat with Flow Bot

* Recipients: Dynamic Content → studnum

* Message: Switch to code view and set values as the dynamic message and url

<img width="1573" height="826" alt="image" src="https://github.com/user-attachments/assets/97caa163-f67b-482a-a4f5-bd56c46c40ae" />


### Save & Collect Webhook URL 🔗

* Click Save

### 🎉 Congrats! You just built your Teams workflow!

#### Scroll to the top and grab your HTTP POST URL.

<img width="1549" height="831" alt="image" src="https://github.com/user-attachments/assets/c723a145-068b-414e-ba00-db5d3802f65f" />

# 🐍 Python Script

## The Python script takes a CSV file of student attendance data and sends each student a personalized Teams message with their notes.

### 📂 CSV File Format

The CSV file is expected to follow this structure:

```bash
Name;First Join;Last Leave;In-Meeting Duration;Email;Participant ID (UPN);Role
Motheo Mkhwanazi;8/20/25, 3:04:05 PM;8/20/25, 4:55:26 PM;1h 51m 21s;1234@school.com;1234@school.com;Presenter

```

* That’s why the script uses:
```python
fullname,FirstJoin,LastLeave,Duration,studNum,Participant,Role = student.split(';')

```

### The split(';') ensures each column is broken into the right variable.You can change this to fit your use case.

## 🎉 Run the code
```python
send_notes_teams(excel_sheet,slides)
```

### Each student gets a personalized Teams message 👋

### It contains their name, a friendly note ✨, and the slides link 📎



 
