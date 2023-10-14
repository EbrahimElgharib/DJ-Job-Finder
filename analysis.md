- job :
    - user [ one-to-many ]
    - title
    - salary
    - location
    - image
    - posted_at
    - application_at
    - vacancy 
    - job_nature
    - description
    - experience

    - company: [ one-to-many ]
        - user [ one-to-one ]***
        - name
        - description
        - website
        - email
        - 


    - category [ one-to-many ]
        - name
        - image