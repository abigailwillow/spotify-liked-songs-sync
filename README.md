# Spotify Liked Songs Sync

1. Clone this repository
2. Install dependencies using `pip install -r requirements.txt`
3. Set [environment variables](#environment-variables), or create `.env` file
4. Run `app.py`
5. Follow the authorization instructions
6. The application will sync your liked songs to the playlist you set, make sure the playlist you chose is public

## Environment Variables

```env
SPOTIPY_CLIENT_ID=YOUR_CLIENT_ID
SPOTIPY_CLIENT_SECRET=YOUR_CLIENT_SECRET
SPOTIPY_REDIRECT_URI=YOUR_REDIRECT_URI
PLAYLIST_URI=YOUR_PLAYLIST_URI
```
