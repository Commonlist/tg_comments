# tg_comments

This repository contains a prototype system for automatic summarization of comments in Telegram. The system monitors the "Favorites" chat for post links, collects comments, and sends them to a GPT bot for generating a concise summary. This helps quickly grasp the main points of discussions.

## Introduction

The `tg_comments` script is designed to make it easier to understand large discussions happening on Telegram by automatically summarizing comments on specific posts. This is particularly useful for busy individuals who want to quickly catch up on the main points without having to read through all the comments.

## Features

- **Monitors Telegram Chat:** The script watches the "Favorites" chat for any links to Telegram posts.
- **Collects Comments:** Once a post link is detected, it collects all the comments from that post.
- **Sends Comments for Summarization:** The collected comments are then sent to a GPT bot, which generates a concise summary of the discussion.
- **Easy Setup and Use:** The script is easy to set up and requires minimal configuration.

## How It Works

1. **Monitoring for Links:**  
   The script runs in the background and monitors a specific chat (your "Favorites" chat) for any links to Telegram posts.

2. **Collecting Comments:**  
   When a link is detected, the script fetches all the comments associated with that post. Each comment is recorded along with the username of the commenter.

3. **Sending Comments for Summarization:**  
   The collected comments are sent to a GPT bot. This bot uses advanced language processing to analyze the comments and generate a summary that captures the main points of the discussion.

4. **Receiving the Summary:**  
   The summary generated by the GPT bot is then sent back to you, allowing you to quickly understand the gist of the conversation.

## Getting Started

### Prerequisites

To use this script, you need to have the following:

- Python 3.8 or higher
- A Telegram account
- API credentials from Telegram (API ID and API Hash)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Commonlist/tg_comments.git
    ```

2. **Install the Required Packages:**  
   Navigate to the project directory and install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Credentials:**  
   You need to set up your API credentials for Telegram. You can find the instructions for obtaining these credentials in the respective documentation of Telegram.

### Configuration

Update the script `tg_comments.py` with your API credentials:

```python
api_id = "your_api_id"
api_hash = "your_api_hash"
```

### Running the Script

To start the script, simply run:

```bash
python tg_comments.py
```

or

```bash
nohup python tg_comments.py &
```

The script will start monitoring your "Favorites" chat for any links to Telegram posts.

## Example Usage

- **Step 1:** Add the link to a Telegram post in your "Favorites" chat.
- **Step 2:** The script detects the link and fetches all comments related to that post.
- **Step 3:** The comments are sent to the GPT bot for summarization.
- **Step 4:** You receive a concise summary of the discussion in the post.

## Troubleshooting

If you encounter any issues while using the script, here are some common troubleshooting steps:

- **Check API Credentials:** Ensure that your API ID and API Hash are correct.
- **Internet Connection:** Make sure your internet connection is stable.
- **Script Errors:** If there are any errors in the script, refer to the error message for more details and fix the mentioned issues.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By using this script, you can save time and quickly understand the key points of discussions happening on Telegram without reading through all the comments.
