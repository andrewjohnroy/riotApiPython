from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('key')

my_region = 'oc1'

me = lol_watcher.summoner.by_name(my_region, 'INGSOC')
# print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)

# First we get the latest version of the game from data dragon
versions = lol_watcher.data_dragon.versions_for_region('oce')
champions_version = versions['n']['champion']

current_champ_list = lol_watcher.data_dragon.champions(champions_version)
# print(current_champ_list)

# try:
#    response = lol_watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
# except ApiError as err:
#    if err.response.status_code == 429:
#        print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
#        print('this retry-after is handled by default by the RiotWatcher library')
#        print('future requests wait until the retry-after time passes')
#    elif err.response.status_code == 404:
#        print('Summoner with that ridiculous name not found.')
#    else:
#        raise
