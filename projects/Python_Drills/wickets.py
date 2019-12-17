matches = [
    {
        'id': 1,
        'season': 2008
    },
    {
        'id': 2,
        'season': 2008
    },
    {
        'id': 3,
        'season': 2009
    }
]
deliveries = [
    {
        'match_id': 1,
        'bowler': 'bowler-1',
        'player_dismissed': 'batsman-1'
    },
    {
        'match_id': 1,
        'bowler': 'bowler-1',
        'player_dismissed': ''
    },
    {
        'match_id': 1,
        'bowler': 'bowler-1',
        'player_dismissed': 'batsman-2'
    },
    {
        'match_id': 1,
        'bowler': 'bowler-1',
        'player_dismissed': 'batsman-3'
    },
    {
        'match_id': 1,
        'bowler': 'bowler-1',
        'player_dismissed': ''
    },
    {
        'match_id': 2,
        'bowler': 'bowler-2',
        'player_dismissed': 'batsman-1'
    },
    {
        'match_id': 2,
        'bowler': 'bowler-2',
        'player_dismissed': ''
    },
    {
        'match_id': 3, 
        'bowler': 'bowler-3',
        'player_dismissed': 'batsman-2'
    },
    {
        'match_id': 3,
        'bowler': 'bowler-3',
        'player_dismissed': 'batsman-3'
    },
    {
        'match_id': 3,
        'bowler': 'bowler-2',
        'player_dismissed': ''
    }
]

expected_output={
    "2008":{"bowler-1":4},
    "2009":{"bowler-3":2}
}
    
season_by_id={}
for match in matches:
    if match['id'] not in season_by_id:
        season_by_id[match['id']]={}
    if match['season'] not in season_by_id[match['id']]:
        season_by_id[match['id']]=match['season']
print (season_by_id)
wickets_by_bowlers={}
for delivery in deliveries:
    if delivery['match_id'] in season_by_id:
        if season_by_id[delivery['match_id']] not in wickets_by_bowlers:
            wickets_by_bowlers[season_by_id[delivery['match_id']]]={}
        if delivery['bowler'] not in wickets_by_bowlers[season_by_id[delivery['match_id']]] and delivery['player_dismissed']!='':
            wickets_by_bowlers[season_by_id[delivery['match_id']]][delivery['bowler']]=0
        if delivery['bowler'] in wickets_by_bowlers[season_by_id[delivery['match_id']]] and delivery['player_dismissed']!='':
            wickets_by_bowlers[season_by_id[delivery['match_id']]][delivery['bowler']]+=1
print (wickets_by_bowlers)       

