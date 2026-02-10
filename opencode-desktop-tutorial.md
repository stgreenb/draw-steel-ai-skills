## Complete Beginner's Guide: Setting Up OpenCode Desktop with the Draw Steel Monster Generator Skill

This tutorial will walk you through installing OpenCode Desktop on Windows 11 and adding the Draw Steel Monster Generator as an Agent Skill. You won't need to use the command line or understand GitHub. [opencode](https://opencode.ai/docs/skills/)

## Download and Install OpenCode Desktop

1. **Download OpenCode Desktop**
   - Visit [https://opencode.ai/download](https://opencode.ai/download) in your web browser
   - Click the "Windows (x64)" download button to get the installer file
   - Wait for the `.exe` file to finish downloading (it will appear in your Downloads folder)

2. **Run the Installer**
   - Double-click the downloaded `.exe` file in your Downloads folder
   - If Windows asks "Do you want to allow this app to make changes?", click **Yes**
   - Follow the installation wizard by clicking **Next** through each screen
   - Leave all default settings as they are unless you want to change the installation location
   - Click **Install** and wait for the installation to complete
   - Click **Finish** when done

3. **Launch OpenCode Desktop**
   - Find "OpenCode Desktop" in your Start Menu and open it
   - The application will take a moment to initialize on first launch

**Good news!** OpenCode Zen offers free models (like GLM 4.7 Free, Kimi K2.5 Free, and others) that you can use at no cost. Many will work well with the monster generator but try differen't ones. If you don't see them avaiblie you try running the `/connect` command in OpenCode and selecting OpenCode Zen. [opencode](https://opencode.ai/docs/zen/)

## Install Node.js (Required for Adding Skills)

OpenCode needs Node.js to install Agent Skills easily. Here's how to install it: [aiengineerguide](https://aiengineerguide.com/blog/add-agent-skills-using-add-skill/)

1. **Download Node.js**
   - Open your web browser and go to [https://nodejs.org](https://nodejs.org)
   - Click the button that says "Download Node.js (LTS)" - this downloads the recommended version
   - Wait for the installer to download

2. **Install Node.js**
   - Double-click the downloaded installer file
   - Click **Next** on the welcome screen
   - Check the box that says "I accept the terms in the License Agreement" and click **Next**
   - Leave the default installation folder and click **Next**
   - On the "Custom Setup" screen, leave everything as default and click **Next**
   - Click **Install** and wait for it to finish
   - Click **Finish**

3. **Restart Your Computer**
   - Restart your computer to ensure Node.js is properly configured
   - This step is important - don't skip it!

## Download the Monster Generator Skill Files

If you are not familiar with GitHub, here's the easiest way to get the skill files:

1. **Visit the GitHub Page**
   - Open your web browser and go to: [https://github.com/stgreenb/draw-steel-monster-generator](https://github.com/stgreenb/draw-steel-monster-generator)

2. **Download the Files**
   - Look for a green button that says **"<> Code"** near the top of the page
   - Click on it and a menu will appear
   - Click **"Download ZIP"** at the bottom of that menu
   - The file will download to your Downloads folder

3. **Extract the Files**
   - Go to your Downloads folder and find the file named `draw-steel-monster-generator-main.zip`
   - Right-click on it and select **"Extract All..."**
   - Click **"Extract"** in the window that appears
   - A new folder will be created with all the skill files inside

## Add the Skill to OpenCode Desktop

Agent Skills are discovered by OpenCode when placed in specific folders. Here's how to set it up: [opencode](https://opencode.ai/docs/skills/)

1. **Open File Explorer**
   - Press the **Windows key + E** on your keyboard to open File Explorer
   - This shows your files and folders

2. **Navigate to Your User Folder**
   - In the left sidebar, click on **"This PC"**
   - Double-click on your **C: drive** (usually called "Windows (C:)")
   - Double-click on the **"Users"** folder
   - Double-click on your username folder (it will have your Windows account name)

3. **Create the OpenCode Skills Folder**
   - In your user folder, you need to create a hidden folder structure. To make this easier, we'll use the address bar
   - Click in the address bar at the top (where it shows the folder path)
   - Type or paste: `%USERPROFILE%\.config\opencode\skills` and press **Enter**
   - If Windows says the folder doesn't exist, click **Yes** to create it
   - (Note: If the `.config` folder doesn't exist, you'll need to create it first - right-click in your user folder, select New > Folder, and name it `.config`)

4. **Copy the Skill Files**
   - Go back to your Downloads folder and find the extracted `draw-steel-monster-generator-main` folder
   - Open that folder - you should see files like `SKILL.md` inside
   - Select all the contents of this folder (press **Ctrl + A**)
   - Copy them (press **Ctrl + C**)
   - Go back to the `%USERPROFILE%\.config\opencode\skills` folder
   - Create a new folder here called `draw-steel-monsters` (right-click > New > Folder)
   - Open the `draw-steel-monsters` folder
   - Paste the files inside (press **Ctrl + V**)

5. **Verify the Setup**
   - Make sure you have a file path that looks like this:
   - `C:\Users\YourName\.config\opencode\skills\draw-steel-monsters\SKILL.md`
   - The `SKILL.md` file is what OpenCode looks for [agentskills](https://agentskills.io/integrate-skills)

## Enable and Use the Skill in OpenCode

1. **Restart OpenCode Desktop**
   - Close OpenCode Desktop completely if it's open
   - Reopen it from your Start Menu
   - OpenCode will automatically discover the new skill at startup [opencode](https://opencode.ai/docs/skills/)

2. **Verify the Skill is Available**
   - Start a new chat or coding session in OpenCode
   - Type: "What skills are available?"
   - OpenCode should list the Draw Steel Monster Generator among available skills [opencode](https://opencode.ai/docs/skills/)

3. **Use the Monster Generator**
   - Simply mention what you want in your prompt, and OpenCode will automatically use the skill when relevant [opencode](https://opencode.ai/docs/skills/)
   - Example: "Create a level 5 undead harrier for Draw Steel"
   - Example: "Use the draw-steel-monsters skill to generate a warrior enemy"
   - OpenCode will load the skill instructions and help you create custom monster stat blocks for your Draw Steel RPG campaigns

## Configure Skill Permissions (Optional)

You can control how OpenCode uses this skill: [youtube](https://www.youtube.com/watch?v=vHkLrDD2xrU)

1. **Open OpenCode Settings**
   - In OpenCode Desktop, look for a settings icon or menu
   - Find the section for skill permissions

2. **Set Permission Level**
   - **Allow**: The skill loads automatically whenever needed (recommended)
   - **Ask**: OpenCode will prompt you before using the skill
   - **Deny**: The skill will be hidden and unavailable

## Troubleshooting

**If OpenCode doesn't see the skill:**
- Make sure the `SKILL.md` file is in the correct location: `%USERPROFILE%\.config\opencode\skills\draw-steel-monsters\SKILL.md`
- Check that the file is named exactly `SKILL.md` (in all capitals) [agentskills](https://agentskills.io/integrate-skills)
- Restart OpenCode Desktop after adding the skill files
- Verify that the `.config` and `opencode` folders exist in your user directory

**If you can't see hidden folders:**
- In File Explorer, click the **View** menu at the top
- Check the box that says **"Hidden items"**
- This will show folders that start with a dot (like `.config`)

**Alternative installation method:**
- If you're comfortable with it after all, you can use the simple command `npx add-skill stgreenb/draw-steel-monster-generator` from Windows PowerShell or Terminal, which will automatically install the skill to the correct location [aiengineerguide](https://aiengineerguide.com/blog/add-agent-skills-using-add-skill/)

This setup gives you access to powerful monster creation tools for Draw Steel directly within OpenCode Desktop, allowing you to quickly generate and customize creatures for your campaigns without needing technical knowledge. [youtube](https://www.youtube.com/watch?v=fabAI1OKKww)
