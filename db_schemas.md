# MODEL/DB FIELDS

## 'LISTING' Table Fields

### id: INT

### realtor: INT (FOREIGN KEY [REALTOR])

### title: STR

### address: STR

### city: STR

### state: STR

### zipcode: STR

### description: TEXT

### price: INT

### bedrooms: INT

### bathrooms: INT

### garage: INT [0]

### sqft: INT

### lot_size: FLOAT

### list_date: DATE

### is_published: BOOL [true]

### photo_main: STR

### photo_1: STR

### photo_2: STR

### photo_3: STR

### photo_4: STR

### photo_5: STR

### photo_6: STR

## 'REALTOR' Table Fields

### id: INT

### name: STR

### photo: STR

### description: TEXT

### email: STR

### phone: STR

### is_mvp: BOOL [0]

### hire_date: DATE

## 'CONTACT' Table Fields

### id: INT

### user_id: INT

### listing: INT

### listing_id: INT

### name: STR

### email: STR

### phone: STR

### message: TEXT

### contact_date: DATE

###
