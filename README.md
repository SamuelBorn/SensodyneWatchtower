# SensodyneWatchtower

A Python script that regularly monitors the Sensodyne Money Back Guarantee website to detect changes in the offer.

Ideal for users who have difficulty securing weekly redemptions due to limited availability.

The script will check every 3 seconds for changes on the Sensodyne website and send a Pushover notification to your Phone if a change is detected.

## Usage

1. Create [Pushover](https://pushover.net/) account, note down _User Key_ and _API Token_ (A trash email can be used for a free trial)
1. Install Pushover app on your phone
1. `git clone https://github.com/SamuelBorn/SensodyneWatchtower.git`
1. `cd SensodyneWatchtower`
1. Edit `.env` file with your Pushover User Key and API Token
1. `pip install -r requirements.txt`
1. `python3 main.py`
