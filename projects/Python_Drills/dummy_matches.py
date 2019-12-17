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
    
    