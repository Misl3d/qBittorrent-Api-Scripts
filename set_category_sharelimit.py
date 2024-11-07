import qbittorrentapi

client = qbittorrentapi.Client(host='127.0.0.1:8080', username='CHANGE_ME', password='CHANGE_ME')

target_tracker_url = "TRACKER_URL"  # Replace with the tracker URL to look for
target_category = "CATEGORY"        # Replace with the category to set

target_ratio = RATIO # float value ex. 10.0
target_time = TIME # in minutes ex. 180 
target_inactive_time = INACTIVE_TIME # in minutes

try:
    torrents = client.torrents_info()

    # Loop through each torrent to check its trackers
    for torrent in torrents:
        trackers = client.torrents_trackers(torrent.hash)
        if any(target_tracker_url in tracker.url for tracker in trackers):
            client.torrents_set_category(hashes=torrent.hash, category=target_category)
            client.torrents_set_share_limits(hashes=torrent.hash, ratio_limit=target_ratio, seeding_time_limit=target_time, inactive_seeding_time_limit=target_inactive_time)
            print(f"Category: {target_category} | Ratio: {target_ratio} | Time Limit: {target_time} mins | Torrent: {torrent.name} | ")


except qbittorrentapi.LoginFailed as e:
    print("Login failed, please check your credentials.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
