if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Helper-Botz/LILSA.git /LILSA
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LILSA
fi
cd /LILSA
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 lilsa.py
