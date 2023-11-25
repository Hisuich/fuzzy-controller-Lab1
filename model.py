input_lvs = [
    {
        'X': (9, 121, 1),
        'name': 'Size (m^2)',
        'terms': {
            'Small': ('trapmf', 9, 9, 15, 20),
            'Medium': ('trapmf', 15, 30, 40, 50),
            'Big': ('trapmf', 40, 50, 70, 85),
            'Huge': ('trapmf', 85, 100, 120, 120)
            
        }
    },

    {
        'X': (0, 101, 1),
        'name': 'Age',
        'terms': {
            'New': ('trapmf', 0, 0, 10, 15),
            'Aged': ('trapmf', 10, 15, 30, 40),
            'Old': ('trapmf', 30, 40, 70, 80),
            'Too Old': ('trapmf', 70, 80, 100, 100)
        }
    },

    {
        'X': (0, 101, 1),
        'name': 'Location',
        'terms': {
            'Terrible': ('trapmf', 0, 0, 10, 25),
            'Bad': ('trapmf', 10, 25, 40, 50),
            'Decent': ('trapmf', 40, 50, 60, 70),
            'Comfortable': ('trapmf', 60, 70, 80, 90),
            'Good': ('trapmf', 80, 90, 100, 100)
        }
    },

    {
        'X': (0, 101, 1),
        'name': 'Infrastructure',
        'terms': {
            'Terrible': ('trapmf', 0, 0, 10, 25),
            'Bad': ('trapmf', 10, 25, 40, 50),
            'Decent': ('trapmf', 40, 50, 60, 70),
            'Comfortable': ('trapmf', 60, 70, 80, 90),
            'Good': ('trapmf', 80, 90, 100, 100),
        }
    }
]

output_lv = {
    'X': (0, 1000000, 0.1),
    'name': 'Estate Price ($)',
    'terms': {
        'Very Low': ('trapmf', 0, 0, 5000, 10000),
        'Low': ('trapmf', 5000, 10000, 25000, 40000),
        'Medium': ('trapmf', 25000, 40000, 80000, 100000),
        'Above medium': ('trapmf', 80000, 100000, 200000, 300000),
        'High': ('trapmf', 200000, 300000, 600000, 700000),
        'Extremely high': ('trapmf', 600000, 700000, 1000000, 1000000),
    }
}


rule_base = [
    (('Small', 'Too Old', 'Terrible', 'Terrible'),      'Very Low'),
    (('Small', 'Too Old', 'Terrible', 'Bad'),           'Very Low'),
    (('Small', 'Too Old', 'Terrible', 'Decent'),        'Very Low'),
    (('Small', 'Too Old', 'Terrible', 'Comfortable'),   'Very Low'),
    (('Small', 'Too Old', 'Terrible', 'Good'),          'Very Low'),

    (('Small', 'Too Old', 'Bad', 'Terrible'),      'Very Low'),
    (('Small', 'Too Old', 'Bad', 'Bad'),           'Very Low'),
    (('Small', 'Too Old', 'Bad', 'Decent'),        'Very Low'),
    (('Small', 'Too Old', 'Bad', 'Comfortable'),   'Very Low'),
    (('Small', 'Too Old', 'Bad', 'Good'),          'Very Low'),

    (('Small', 'Too Old', 'Decent', 'Terrible'),      'Very Low'),
    (('Small', 'Too Old', 'Decent', 'Bad'),           'Very Low'),
    (('Small', 'Too Old', 'Decent', 'Decent'),        'Very Low'),
    (('Small', 'Too Old', 'Decent', 'Comfortable'),   'Very Low'),
    (('Small', 'Too Old', 'Decent', 'Good'),          'Low'),

    (('Small', 'Too Old', 'Comfortable', 'Terrible'),      'Very Low'),
    (('Small', 'Too Old', 'Comfortable', 'Bad'),           'Very Low'),
    (('Small', 'Too Old', 'Comfortable', 'Decent'),        'Very Low'),
    (('Small', 'Too Old', 'Comfortable', 'Comfortable'),   'Low'),
    (('Small', 'Too Old', 'Comfortable', 'Good'),          'Low'),

    (('Small', 'Too Old', 'Good', 'Terrible'),      'Very Low'),
    (('Small', 'Too Old', 'Good', 'Bad'),           'Very Low'),
    (('Small', 'Too Old', 'Good', 'Decent'),        'Low'),
    (('Small', 'Too Old', 'Good', 'Comfortable'),   'Low'),
    (('Small', 'Too Old', 'Good', 'Good'),          'Low'),
###################################################################
    (('Small', 'Old', 'Terrible', 'Terrible'),      'Very Low'),
    (('Small', 'Old', 'Terrible', 'Bad'),           'Very Low'),
    (('Small', 'Old', 'Terrible', 'Decent'),        'Very Low'),
    (('Small', 'Old', 'Terrible', 'Comfortable'),   'Very Low'),
    (('Small', 'Old', 'Terrible', 'Good'),          'Very Low'),

    (('Small', 'Old', 'Bad', 'Terrible'),      'Very Low'),
    (('Small', 'Old', 'Bad', 'Bad'),           'Very Low'),
    (('Small', 'Old', 'Bad', 'Decent'),        'Very Low'),
    (('Small', 'Old', 'Bad', 'Comfortable'),   'Very Low'),
    (('Small', 'Old', 'Bad', 'Good'),          'Low'),

    (('Small', 'Old', 'Decent', 'Terrible'),      'Very Low'),
    (('Small', 'Old', 'Decent', 'Bad'),           'Very Low'),
    (('Small', 'Old', 'Decent', 'Decent'),        'Very Low'),
    (('Small', 'Old', 'Decent', 'Comfortable'),   'Low'),
    (('Small', 'Old', 'Decent', 'Good'),          'Low'),

    (('Small', 'Old', 'Comfortable', 'Terrible'),      'Very Low'),
    (('Small', 'Old', 'Comfortable', 'Bad'),           'Very Low'),
    (('Small', 'Old', 'Comfortable', 'Decent'),        'Low'),
    (('Small', 'Old', 'Comfortable', 'Comfortable'),   'Low'),
    (('Small', 'Old', 'Comfortable', 'Good'),          'Low'),

    (('Small', 'Old', 'Good', 'Terrible'),      'Very Low'),
    (('Small', 'Old', 'Good', 'Bad'),           'Low'),
    (('Small', 'Old', 'Good', 'Decent'),        'Low'),
    (('Small', 'Old', 'Good', 'Comfortable'),   'Low'),
    (('Small', 'Old', 'Good', 'Good'),          'Low'),
###################################################################
    (('Small', 'Aged', 'Terrible', 'Terrible'),      'Very Low'),
    (('Small', 'Aged', 'Terrible', 'Bad'),           'Very Low'),
    (('Small', 'Aged', 'Terrible', 'Decent'),        'Very Low'),
    (('Small', 'Aged', 'Terrible', 'Comfortable'),   'Very Low'),
    (('Small', 'Aged', 'Terrible', 'Good'),          'Low'),

    (('Small', 'Aged', 'Bad', 'Terrible'),      'Very Low'),
    (('Small', 'Aged', 'Bad', 'Bad'),           'Very Low'),
    (('Small', 'Aged', 'Bad', 'Decent'),        'Very Low'),
    (('Small', 'Aged', 'Bad', 'Comfortable'),   'Low'),
    (('Small', 'Aged', 'Bad', 'Good'),          'Low'),

    (('Small', 'Aged', 'Decent', 'Terrible'),      'Very Low'),
    (('Small', 'Aged', 'Decent', 'Bad'),           'Very Low'),
    (('Small', 'Aged', 'Decent', 'Decent'),        'Low'),
    (('Small', 'Aged', 'Decent', 'Comfortable'),   'Low'),
    (('Small', 'Aged', 'Decent', 'Good'),          'Low'),

    (('Small', 'Aged', 'Comfortable', 'Terrible'),      'Very Low'),
    (('Small', 'Aged', 'Comfortable', 'Bad'),           'Low'),
    (('Small', 'Aged', 'Comfortable', 'Decent'),        'Low'),
    (('Small', 'Aged', 'Comfortable', 'Comfortable'),   'Low'),
    (('Small', 'Aged', 'Comfortable', 'Good'),          'Low'),

    (('Small', 'Aged', 'Good', 'Terrible'),      'Low'),
    (('Small', 'Aged', 'Good', 'Bad'),           'Low'),
    (('Small', 'Aged', 'Good', 'Decent'),        'Low'),
    (('Small', 'Aged', 'Good', 'Comfortable'),   'Low'),
    (('Small', 'Aged', 'Good', 'Good'),          'Low'),    
######################################################################    
    (('Small', 'New', 'Terrible', 'Terrible'),      'Very Low'),
    (('Small', 'New', 'Terrible', 'Bad'),           'Very Low'),
    (('Small', 'New', 'Terrible', 'Decent'),        'Very Low'),
    (('Small', 'New', 'Terrible', 'Comfortable'),   'Low'),
    (('Small', 'New', 'Terrible', 'Good'),          'Low'),

    (('Small', 'New', 'Bad', 'Terrible'),      'Very Low'),
    (('Small', 'New', 'Bad', 'Bad'),           'Very Low'),
    (('Small', 'New', 'Bad', 'Decent'),        'Low'),
    (('Small', 'New', 'Bad', 'Comfortable'),   'Low'),
    (('Small', 'New', 'Bad', 'Good'),          'Low'),

    (('Small', 'New', 'Decent', 'Terrible'),      'Very Low'),
    (('Small', 'New', 'Decent', 'Bad'),           'Low'),
    (('Small', 'New', 'Decent', 'Decent'),        'Low'),
    (('Small', 'New', 'Decent', 'Comfortable'),   'Low'),
    (('Small', 'New', 'Decent', 'Good'),          'Low'),

    (('Small', 'New', 'Comfortable', 'Terrible'),      'Low'),
    (('Small', 'New', 'Comfortable', 'Bad'),           'Low'),
    (('Small', 'New', 'Comfortable', 'Decent'),        'Low'),
    (('Small', 'New', 'Comfortable', 'Comfortable'),   'Low'),
    (('Small', 'New', 'Comfortable', 'Good'),          'Low'),

    (('Small', 'New', 'Good', 'Terrible'),      'Low'),
    (('Small', 'New', 'Good', 'Bad'),           'Low'),
    (('Small', 'New', 'Good', 'Decent'),        'Low'),
    (('Small', 'New', 'Good', 'Comfortable'),   'Low'),
    (('Small', 'New', 'Good', 'Good'),          'Medium'),       
#######################################################################
#=====================================================================#    
    (('Medium', 'Too Old', 'Terrible', 'Terrible'),      'Very Low'),
    (('Medium', 'Too Old', 'Terrible', 'Bad'),           'Very Low'),
    (('Medium', 'Too Old', 'Terrible', 'Decent'),        'Low'),
    (('Medium', 'Too Old', 'Terrible', 'Comfortable'),   'Low'),
    (('Medium', 'Too Old', 'Terrible', 'Good'),          'Low'),

    (('Medium', 'Too Old', 'Bad', 'Terrible'),      'Very Low'),
    (('Medium', 'Too Old', 'Bad', 'Bad'),           'Low'),
    (('Medium', 'Too Old', 'Bad', 'Decent'),        'Low'),
    (('Medium', 'Too Old', 'Bad', 'Comfortable'),   'Low'),
    (('Medium', 'Too Old', 'Bad', 'Good'),          'Low'),

    (('Medium', 'Too Old', 'Decent', 'Terrible'),      'Low'),
    (('Medium', 'Too Old', 'Decent', 'Bad'),           'Low'),
    (('Medium', 'Too Old', 'Decent', 'Decent'),        'Low'),
    (('Medium', 'Too Old', 'Decent', 'Comfortable'),   'Low'),
    (('Medium', 'Too Old', 'Decent', 'Good'),          'Low'),

    (('Medium', 'Too Old', 'Comfortable', 'Terrible'),      'Low'),
    (('Medium', 'Too Old', 'Comfortable', 'Bad'),           'Low'),
    (('Medium', 'Too Old', 'Comfortable', 'Decent'),        'Low'),
    (('Medium', 'Too Old', 'Comfortable', 'Comfortable'),   'Low'),
    (('Medium', 'Too Old', 'Comfortable', 'Good'),          'Medium'),

    (('Medium', 'Too Old', 'Good', 'Terrible'),      'Low'),
    (('Medium', 'Too Old', 'Good', 'Bad'),           'Low'),
    (('Medium', 'Too Old', 'Good', 'Decent'),        'Low'),
    (('Medium', 'Too Old', 'Good', 'Comfortable'),   'Medium'),
    (('Medium', 'Too Old', 'Good', 'Good'),          'Medium'),
###################################################################
    (('Medium', 'Old', 'Terrible', 'Terrible'),      'Very Low'),
    (('Medium', 'Old', 'Terrible', 'Bad'),           'Low'),
    (('Medium', 'Old', 'Terrible', 'Decent'),        'Low'),
    (('Medium', 'Old', 'Terrible', 'Comfortable'),   'Low'),
    (('Medium', 'Old', 'Terrible', 'Good'),          'Low'),

    (('Medium', 'Old', 'Bad', 'Terrible'),      'Low'),
    (('Medium', 'Old', 'Bad', 'Bad'),           'Low'),
    (('Medium', 'Old', 'Bad', 'Decent'),        'Low'),
    (('Medium', 'Old', 'Bad', 'Comfortable'),   'Low'),
    (('Medium', 'Old', 'Bad', 'Good'),          'Low'),

    (('Medium', 'Old', 'Decent', 'Terrible'),      'Low'),
    (('Medium', 'Old', 'Decent', 'Bad'),           'Low'),
    (('Medium', 'Old', 'Decent', 'Decent'),        'Low'),
    (('Medium', 'Old', 'Decent', 'Comfortable'),   'Low'),
    (('Medium', 'Old', 'Decent', 'Good'),          'Medium'),

    (('Medium', 'Old', 'Comfortable', 'Terrible'),      'Low'),
    (('Medium', 'Old', 'Comfortable', 'Bad'),           'Low'),
    (('Medium', 'Old', 'Comfortable', 'Decent'),        'Low'),
    (('Medium', 'Old', 'Comfortable', 'Comfortable'),   'Medium'),
    (('Medium', 'Old', 'Comfortable', 'Good'),          'Medium'),

    (('Medium', 'Old', 'Good', 'Terrible'),      'Low'),
    (('Medium', 'Old', 'Good', 'Bad'),           'Low'),
    (('Medium', 'Old', 'Good', 'Decent'),        'Medium'),
    (('Medium', 'Old', 'Good', 'Comfortable'),   'Medium'),
    (('Medium', 'Old', 'Good', 'Good'),          'Medium'),
###################################################################
    (('Medium', 'Aged', 'Terrible', 'Terrible'),      'Low'),
    (('Medium', 'Aged', 'Terrible', 'Bad'),           'Low'),
    (('Medium', 'Aged', 'Terrible', 'Decent'),        'Low'),
    (('Medium', 'Aged', 'Terrible', 'Comfortable'),   'Low'),
    (('Medium', 'Aged', 'Terrible', 'Good'),          'Low'),

    (('Medium', 'Aged', 'Bad', 'Terrible'),      'Low'),
    (('Medium', 'Aged', 'Bad', 'Bad'),           'Low'),
    (('Medium', 'Aged', 'Bad', 'Decent'),        'Low'),
    (('Medium', 'Aged', 'Bad', 'Comfortable'),   'Low'),
    (('Medium', 'Aged', 'Bad', 'Good'),          'Medium'),

    (('Medium', 'Aged', 'Decent', 'Terrible'),      'Low'),
    (('Medium', 'Aged', 'Decent', 'Bad'),           'Low'),
    (('Medium', 'Aged', 'Decent', 'Decent'),        'Low'),
    (('Medium', 'Aged', 'Decent', 'Comfortable'),   'Medium'),
    (('Medium', 'Aged', 'Decent', 'Good'),          'Medium'),

    (('Medium', 'Aged', 'Comfortable', 'Terrible'),      'Low'),
    (('Medium', 'Aged', 'Comfortable', 'Bad'),           'Low'),
    (('Medium', 'Aged', 'Comfortable', 'Decent'),        'Medium'),
    (('Medium', 'Aged', 'Comfortable', 'Comfortable'),   'Medium'),
    (('Medium', 'Aged', 'Comfortable', 'Good'),          'Medium'),

    (('Medium', 'Aged', 'Good', 'Terrible'),      'Low'),
    (('Medium', 'Aged', 'Good', 'Bad'),           'Medium'),
    (('Medium', 'Aged', 'Good', 'Decent'),        'Medium'),
    (('Medium', 'Aged', 'Good', 'Comfortable'),   'Medium'),
    (('Medium', 'Aged', 'Good', 'Good'),          'Medium'),    
######################################################################    
    (('Medium', 'New', 'Terrible', 'Terrible'),      'Low'),
    (('Medium', 'New', 'Terrible', 'Bad'),           'Low'),
    (('Medium', 'New', 'Terrible', 'Decent'),        'Low'),
    (('Medium', 'New', 'Terrible', 'Comfortable'),   'Low'),
    (('Medium', 'New', 'Terrible', 'Good'),          'Medium'),

    (('Medium', 'New', 'Bad', 'Terrible'),      'Low'),
    (('Medium', 'New', 'Bad', 'Bad'),           'Low'),
    (('Medium', 'New', 'Bad', 'Decent'),        'Low'),
    (('Medium', 'New', 'Bad', 'Comfortable'),   'Medium'),
    (('Medium', 'New', 'Bad', 'Good'),          'Medium'),

    (('Medium', 'New', 'Decent', 'Terrible'),      'Low'),
    (('Medium', 'New', 'Decent', 'Bad'),           'Low'),
    (('Medium', 'New', 'Decent', 'Decent'),        'Medium'),
    (('Medium', 'New', 'Decent', 'Comfortable'),   'Medium'),
    (('Medium', 'New', 'Decent', 'Good'),          'Medium'),

    (('Medium', 'New', 'Comfortable', 'Terrible'),      'Low'),
    (('Medium', 'New', 'Comfortable', 'Bad'),           'Medium'),
    (('Medium', 'New', 'Comfortable', 'Decent'),        'Medium'),
    (('Medium', 'New', 'Comfortable', 'Comfortable'),   'Medium'),
    (('Medium', 'New', 'Comfortable', 'Good'),          'Medium'),

    (('Medium', 'New', 'Good', 'Terrible'),      'Medium'),
    (('Medium', 'New', 'Good', 'Bad'),           'Medium'),
    (('Medium', 'New', 'Good', 'Decent'),        'Medium'),
    (('Medium', 'New', 'Good', 'Comfortable'),   'Medium'),
    (('Medium', 'New', 'Good', 'Good'),          'Medium'),
#####################################################################
#===================================================================#
    (('Big', 'Too Old', 'Terrible', 'Terrible'),      'Low'),
    (('Big', 'Too Old', 'Terrible', 'Bad'),           'Low'),
    (('Big', 'Too Old', 'Terrible', 'Decent'),        'Low'),
    (('Big', 'Too Old', 'Terrible', 'Comfortable'),   'Medium'),
    (('Big', 'Too Old', 'Terrible', 'Good'),          'Medium'),

    (('Big', 'Too Old', 'Bad', 'Terrible'),      'Low'),
    (('Big', 'Too Old', 'Bad', 'Bad'),           'Low'),
    (('Big', 'Too Old', 'Bad', 'Decent'),        'Medium'),
    (('Big', 'Too Old', 'Bad', 'Comfortable'),   'Medium'),
    (('Big', 'Too Old', 'Bad', 'Good'),          'Medium'),

    (('Big', 'Too Old', 'Decent', 'Terrible'),      'Low'),
    (('Big', 'Too Old', 'Decent', 'Bad'),           'Medium'),
    (('Big', 'Too Old', 'Decent', 'Decent'),        'Medium'),
    (('Big', 'Too Old', 'Decent', 'Comfortable'),   'Medium'),
    (('Big', 'Too Old', 'Decent', 'Good'),          'Medium'),

    (('Big', 'Too Old', 'Comfortable', 'Terrible'),      'Medium'),
    (('Big', 'Too Old', 'Comfortable', 'Bad'),           'Medium'),
    (('Big', 'Too Old', 'Comfortable', 'Decent'),        'Medium'),
    (('Big', 'Too Old', 'Comfortable', 'Comfortable'),   'Medium'),
    (('Big', 'Too Old', 'Comfortable', 'Good'),          'Medium'),

    (('Big', 'Too Old', 'Good', 'Terrible'),      'Medium'),
    (('Big', 'Too Old', 'Good', 'Bad'),           'Medium'),
    (('Big', 'Too Old', 'Good', 'Decent'),        'Medium'),
    (('Big', 'Too Old', 'Good', 'Comfortable'),   'Medium'),
    (('Big', 'Too Old', 'Good', 'Good'),          'High'),
###################################################################
    (('Big', 'Old', 'Terrible', 'Terrible'),      'Low'),
    (('Big', 'Old', 'Terrible', 'Bad'),           'Low'),
    (('Big', 'Old', 'Terrible', 'Decent'),        'Medium'),
    (('Big', 'Old', 'Terrible', 'Comfortable'),   'Medium'),
    (('Big', 'Old', 'Terrible', 'Good'),          'Medium'),

    (('Big', 'Old', 'Bad', 'Terrible'),      'Low'),
    (('Big', 'Old', 'Bad', 'Bad'),           'Medium'),
    (('Big', 'Old', 'Bad', 'Decent'),        'Medium'),
    (('Big', 'Old', 'Bad', 'Comfortable'),   'Medium'),
    (('Big', 'Old', 'Bad', 'Good'),          'Medium'),

    (('Big', 'Old', 'Decent', 'Terrible'),      'Medium'),
    (('Big', 'Old', 'Decent', 'Bad'),           'Medium'),
    (('Big', 'Old', 'Decent', 'Decent'),        'Medium'),
    (('Big', 'Old', 'Decent', 'Comfortable'),   'Medium'),
    (('Big', 'Old', 'Decent', 'Good'),          'Medium'),

    (('Big', 'Old', 'Comfortable', 'Terrible'),      'Medium'),
    (('Big', 'Old', 'Comfortable', 'Bad'),           'Medium'),
    (('Big', 'Old', 'Comfortable', 'Decent'),        'Medium'),
    (('Big', 'Old', 'Comfortable', 'Comfortable'),   'Medium'),
    (('Big', 'Old', 'Comfortable', 'Good'),          'High'),

    (('Big', 'Old', 'Good', 'Terrible'),      'Medium'),
    (('Big', 'Old', 'Good', 'Bad'),           'Medium'),
    (('Big', 'Old', 'Good', 'Decent'),        'Medium'),
    (('Big', 'Old', 'Good', 'Comfortable'),   'High'),
    (('Big', 'Old', 'Good', 'Good'),          'High'),
###################################################################
    (('Big', 'Aged', 'Terrible', 'Terrible'),      'Low'),
    (('Big', 'Aged', 'Terrible', 'Bad'),           'Medium'),
    (('Big', 'Aged', 'Terrible', 'Decent'),        'Medium'),
    (('Big', 'Aged', 'Terrible', 'Comfortable'),   'Medium'),
    (('Big', 'Aged', 'Terrible', 'Good'),          'Medium'),

    (('Big', 'Aged', 'Bad', 'Terrible'),      'Medium'),
    (('Big', 'Aged', 'Bad', 'Bad'),           'Medium'),
    (('Big', 'Aged', 'Bad', 'Decent'),        'Medium'),
    (('Big', 'Aged', 'Bad', 'Comfortable'),   'Medium'),
    (('Big', 'Aged', 'Bad', 'Good'),          'Medium'),

    (('Big', 'Aged', 'Decent', 'Terrible'),      'Medium'),
    (('Big', 'Aged', 'Decent', 'Bad'),           'Medium'),
    (('Big', 'Aged', 'Decent', 'Decent'),        'Medium'),
    (('Big', 'Aged', 'Decent', 'Comfortable'),   'Medium'),
    (('Big', 'Aged', 'Decent', 'Good'),          'High'),

    (('Big', 'Aged', 'Comfortable', 'Terrible'),      'Medium'),
    (('Big', 'Aged', 'Comfortable', 'Bad'),           'Medium'),
    (('Big', 'Aged', 'Comfortable', 'Decent'),        'Medium'),
    (('Big', 'Aged', 'Comfortable', 'Comfortable'),   'High'),
    (('Big', 'Aged', 'Comfortable', 'Good'),          'High'),

    (('Big', 'Aged', 'Good', 'Terrible'),      'Medium'),
    (('Big', 'Aged', 'Good', 'Bad'),           'Medium'),
    (('Big', 'Aged', 'Good', 'Decent'),        'High'),
    (('Big', 'Aged', 'Good', 'Comfortable'),   'High'),
    (('Big', 'Aged', 'Good', 'Good'),          'High'),    
######################################################################    
    (('Big', 'New', 'Terrible', 'Terrible'),      'Medium'),
    (('Big', 'New', 'Terrible', 'Bad'),           'Medium'),
    (('Big', 'New', 'Terrible', 'Decent'),        'Medium'),
    (('Big', 'New', 'Terrible', 'Comfortable'),   'Medium'),
    (('Big', 'New', 'Terrible', 'Good'),          'Medium'),

    (('Big', 'New', 'Bad', 'Terrible'),      'Medium'),
    (('Big', 'New', 'Bad', 'Bad'),           'Medium'),
    (('Big', 'New', 'Bad', 'Decent'),        'Medium'),
    (('Big', 'New', 'Bad', 'Comfortable'),   'Medium'),
    (('Big', 'New', 'Bad', 'Good'),          'High'),

    (('Big', 'New', 'Decent', 'Terrible'),      'Medium'),
    (('Big', 'New', 'Decent', 'Bad'),           'Medium'),
    (('Big', 'New', 'Decent', 'Decent'),        'Medium'),
    (('Big', 'New', 'Decent', 'Comfortable'),   'High'),
    (('Big', 'New', 'Decent', 'Good'),          'High'),

    (('Big', 'New', 'Comfortable', 'Terrible'),      'Medium'),
    (('Big', 'New', 'Comfortable', 'Bad'),           'Medium'),
    (('Big', 'New', 'Comfortable', 'Decent'),        'High'),
    (('Big', 'New', 'Comfortable', 'Comfortable'),   'High'),
    (('Big', 'New', 'Comfortable', 'Good'),          'High'),

    (('Big', 'New', 'Good', 'Terrible'),      'Medium'),
    (('Big', 'New', 'Good', 'Bad'),           'High'),
    (('Big', 'New', 'Good', 'Decent'),        'High'),
    (('Big', 'New', 'Good', 'Comfortable'),   'High'),
    (('Big', 'New', 'Good', 'Good'),          'High'),
#########################################################################
#=======================================================================#
    (('Huge', 'Too Old', 'Terrible', 'Terrible'),      'Medium'),
    (('Huge', 'Too Old', 'Terrible', 'Bad'),           'Medium'),
    (('Huge', 'Too Old', 'Terrible', 'Decent'),        'Medium'),
    (('Huge', 'Too Old', 'Terrible', 'Comfortable'),   'Medium'),
    (('Huge', 'Too Old', 'Terrible', 'Good'),          'High'),

    (('Huge', 'Too Old', 'Bad', 'Terrible'),      'Medium'),
    (('Huge', 'Too Old', 'Bad', 'Bad'),           'Medium'),
    (('Huge', 'Too Old', 'Bad', 'Decent'),        'Medium'),
    (('Huge', 'Too Old', 'Bad', 'Comfortable'),   'High'),
    (('Huge', 'Too Old', 'Bad', 'Good'),          'High'),

    (('Huge', 'Too Old', 'Decent', 'Terrible'),      'Medium'),
    (('Huge', 'Too Old', 'Decent', 'Bad'),           'Medium'),
    (('Huge', 'Too Old', 'Decent', 'Decent'),        'High'),
    (('Huge', 'Too Old', 'Decent', 'Comfortable'),   'High'),
    (('Huge', 'Too Old', 'Decent', 'Good'),          'High'),

    (('Huge', 'Too Old', 'Comfortable', 'Terrible'),      'Medium'),
    (('Huge', 'Too Old', 'Comfortable', 'Bad'),           'High'),
    (('Huge', 'Too Old', 'Comfortable', 'Decent'),        'High'),
    (('Huge', 'Too Old', 'Comfortable', 'Comfortable'),   'High'),
    (('Huge', 'Too Old', 'Comfortable', 'Good'),          'High'),

    (('Huge', 'Too Old', 'Good', 'Terrible'),      'High'),
    (('Huge', 'Too Old', 'Good', 'Bad'),           'High'),
    (('Huge', 'Too Old', 'Good', 'Decent'),        'High'),
    (('Huge', 'Too Old', 'Good', 'Comfortable'),   'High'),
    (('Huge', 'Too Old', 'Good', 'Good'),          'Extremely high'),
###################################################################
    (('Huge', 'Old', 'Terrible', 'Terrible'),      'Medium'),
    (('Huge', 'Old', 'Terrible', 'Bad'),           'Medium'),
    (('Huge', 'Old', 'Terrible', 'Decent'),        'Medium'),
    (('Huge', 'Old', 'Terrible', 'Comfortable'),   'High'),
    (('Huge', 'Old', 'Terrible', 'Good'),          'High'),

    (('Huge', 'Old', 'Bad', 'Terrible'),      'Medium'),
    (('Huge', 'Old', 'Bad', 'Bad'),           'Medium'),
    (('Huge', 'Old', 'Bad', 'Decent'),        'High'),
    (('Huge', 'Old', 'Bad', 'Comfortable'),   'High'),
    (('Huge', 'Old', 'Bad', 'Good'),          'High'),

    (('Huge', 'Old', 'Decent', 'Terrible'),      'Medium'),
    (('Huge', 'Old', 'Decent', 'Bad'),           'High'),
    (('Huge', 'Old', 'Decent', 'Decent'),        'High'),
    (('Huge', 'Old', 'Decent', 'Comfortable'),   'High'),
    (('Huge', 'Old', 'Decent', 'Good'),          'High'),

    (('Huge', 'Old', 'Comfortable', 'Terrible'),      'High'),
    (('Huge', 'Old', 'Comfortable', 'Bad'),           'High'),
    (('Huge', 'Old', 'Comfortable', 'Decent'),        'High'),
    (('Huge', 'Old', 'Comfortable', 'Comfortable'),   'High'),
    (('Huge', 'Old', 'Comfortable', 'Good'),          'Extremely high'),

    (('Huge', 'Old', 'Good', 'Terrible'),      'High'),
    (('Huge', 'Old', 'Good', 'Bad'),           'High'),
    (('Huge', 'Old', 'Good', 'Decent'),        'High'),
    (('Huge', 'Old', 'Good', 'Comfortable'),   'Extremely high'),
    (('Huge', 'Old', 'Good', 'Good'),          'Extremely high'),
###################################################################
    (('Huge', 'Aged', 'Terrible', 'Terrible'),      'Medium'),
    (('Huge', 'Aged', 'Terrible', 'Bad'),           'Medium'),
    (('Huge', 'Aged', 'Terrible', 'Decent'),        'High'),
    (('Huge', 'Aged', 'Terrible', 'Comfortable'),   'High'),
    (('Huge', 'Aged', 'Terrible', 'Good'),          'High'),

    (('Huge', 'Aged', 'Bad', 'Terrible'),      'Medium'),
    (('Huge', 'Aged', 'Bad', 'Bad'),           'High'),
    (('Huge', 'Aged', 'Bad', 'Decent'),        'High'),
    (('Huge', 'Aged', 'Bad', 'Comfortable'),   'High'),
    (('Huge', 'Aged', 'Bad', 'Good'),          'High'),

    (('Huge', 'Aged', 'Decent', 'Terrible'),      'High'),
    (('Huge', 'Aged', 'Decent', 'Bad'),           'High'),
    (('Huge', 'Aged', 'Decent', 'Decent'),        'High'),
    (('Huge', 'Aged', 'Decent', 'Comfortable'),   'High'),
    (('Huge', 'Aged', 'Decent', 'Good'),          'Extremely high'),

    (('Huge', 'Aged', 'Comfortable', 'Terrible'),      'High'),
    (('Huge', 'Aged', 'Comfortable', 'Bad'),           'High'),
    (('Huge', 'Aged', 'Comfortable', 'Decent'),        'High'),
    (('Huge', 'Aged', 'Comfortable', 'Comfortable'),   'Extremely high'),
    (('Huge', 'Aged', 'Comfortable', 'Good'),          'Extremely high'),

    (('Huge', 'Aged', 'Good', 'Terrible'),      'High'),
    (('Huge', 'Aged', 'Good', 'Bad'),           'High'),
    (('Huge', 'Aged', 'Good', 'Decent'),        'Extremely high'),
    (('Huge', 'Aged', 'Good', 'Comfortable'),   'Extremely high'),
    (('Huge', 'Aged', 'Good', 'Good'),          'Extremely high'),    
######################################################################    
    (('Huge', 'New', 'Terrible', 'Terrible'),      'Medium'),
    (('Huge', 'New', 'Terrible', 'Bad'),           'High'),
    (('Huge', 'New', 'Terrible', 'Decent'),        'High'),
    (('Huge', 'New', 'Terrible', 'Comfortable'),   'High'),
    (('Huge', 'New', 'Terrible', 'Good'),          'High'),

    (('Huge', 'New', 'Bad', 'Terrible'),      'High'),
    (('Huge', 'New', 'Bad', 'Bad'),           'High'),
    (('Huge', 'New', 'Bad', 'Decent'),        'High'),
    (('Huge', 'New', 'Bad', 'Comfortable'),   'High'),
    (('Huge', 'New', 'Bad', 'Good'),          'High'),

    (('Huge', 'New', 'Decent', 'Terrible'),      'High'),
    (('Huge', 'New', 'Decent', 'Bad'),           'High'),
    (('Huge', 'New', 'Decent', 'Decent'),        'High'),
    (('Huge', 'New', 'Decent', 'Comfortable'),   'Extremely high'),
    (('Huge', 'New', 'Decent', 'Good'),          'Extremely high'),

    (('Huge', 'New', 'Comfortable', 'Terrible'),      'High'),
    (('Huge', 'New', 'Comfortable', 'Bad'),           'High'),
    (('Huge', 'New', 'Comfortable', 'Decent'),        'Extremely high'),
    (('Huge', 'New', 'Comfortable', 'Comfortable'),   'Extremely high'),
    (('Huge', 'New', 'Comfortable', 'Good'),          'Extremely high'),

    (('Huge', 'New', 'Good', 'Terrible'),      'High'),
    (('Huge', 'New', 'Good', 'Bad'),           'Extremely high'),
    (('Huge', 'New', 'Good', 'Decent'),        'Extremely high'),
    (('Huge', 'New', 'Good', 'Comfortable'),   'Extremely high'),
    (('Huge', 'New', 'Good', 'Good'),          'Extremely high'), 
]
