
def get_profile(*args, **kwargs) -> dict:
    """get_profile

    Raises:
        TypeError: if no args are passed or only one arg is passed
        ValueError: age value is not an int
        ValueError: to many sports added

    Example:
        >>> get_profile('john', 5)
        {
            'name': 'john',
            'age': 5
        }
        >>> get_profile('john', 5, 'football')
        {
            'name': 'john',
            'age':5,
            'sports': ['football']
        }
        >>> get_profile('john', 5, 'football', champ='winning goal')
        {
            'name':'john',
            'age':5,
            'sports':['football'],
            'awards':{
                'champ':'winning goal'
            }
        }
    Returns:
        dict:
    """
    try:
        if len(args) < 2:
            raise TypeError('not enough arguments passed')
        
        name = args[0]
        age = args[1]
        
        if type(age) != int:
            raise ValueError('age value is not an int')
        profile = {
            'name': name,
            'age': age
        }
        
        sport = [i for i in args[2:]]
        if len(sport) > 5:
            raise ValueError('to many sports added')
        profile['sports'] = sport
        
        if kwargs:
            profile['awards'] = kwargs
        return profile
        
    except Exception as e:
        raise e