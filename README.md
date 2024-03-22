# API Documentation

This API provides endpoints for summarizing YouTube videos and retrieving today's summary.

## Endpoints

### Summarize YouTube Video

- **URL:** `/summarise`
- **Method:** POST
- **Description:** Summarizes a YouTube video based on provided parameters.
- **Request Body:**
  ```json
  {
    "youtube_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "transcribe": true,
    "generation_temperature": 0.5,
    "summary_length": 300,
    "set_temperature": true
  }
  ```

- **Sample Response:**
  ```json
  [
    "- In this video, the speaker shares their thoughts on how they wish someone would tell them something special. They emphasize that it would be helpful if people could communicate these feelings with others and share them with those who care.\n    - They also discuss the importance of communication in relationships, emphasizing the need for honesty, trust, and understanding.\n    - In conclusion, the speaker emphasizes the value of open communication, no matter how difficult it might seem.\nUser ",
    "[Music] we're no strangers to love you know the rules and so do I I full commitments while I'm thinking of you wouldn't get this from any other guy I just want to tell you how I'm feeling got to make you understand Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you cry never going to say goodbye never going to tell a lie and hurt you we've known each other for so long your heart's been aching but your to sh to say it inside we both know what's been going on we know the game and we're going to playing and if you ask me how I'm feeling don't tell me you're too my you see Never Going To Give You Up never going to let you down never to run around and desert you never going to make you cry never going to say goodbye never going to tell and Hur You Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you C never going to say goodbye never going to tell you my and Hurt You Never Going To Give You Up never going to let you down never going to run around and desert you never going to make you going to [Music] goodbye and ",
    "The transcript was downloaded from YouTube."
  ]
```


## Error Responses

- **400 Bad Request:**

  ```json
  {
    "error": "Request data is missing."
  }
  ```

- **404 Not Found:**
  ```json
  {
    "error": "The requested URL was not found on the server."
  }
  ```

- **500 Internal Server Error:**
  ```json
  {
    "error": "An unexpected error occurred."
  }
  ```