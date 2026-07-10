Overall flow
manage.py runserver
        │
        ▼
settings.py loads
        │
        ▼
Installed Apps loaded
        │
        ▼
AccountsConfig.ready()
        │
        ▼
initialize_database()
        │
        ▼
MongoEngine connect()
        │
        ▼
MongoDB Connection Pool Created
        │
        ▼
Application Starts
        │
        ▼
Views → Models → MongoDB


Architecture

                Django
                  │
                  │
          Request arrives
                  │
                  ▼
               View
                  │
                  ▼
         MongoEngine Document
                  │
                  ▼
      MongoEngine ODM converts
                  │
                  ▼
            MongoDB Query
                  │
                  ▼
             MongoDB Server



Step 1: Define the variable in .env

Create a .env file in your project root:

MONGODB_URI=mongodb://localhost:27017/blog

or for MongoDB Atlas:

MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/blog
Step 2: Read it in Python
from decouple import config

mongodb_uri = config("MONGODB_URI")

Here,

config() is provided by the python-decouple package.
It looks for a variable named MONGODB_URI in your environment or .env file.

If it finds it:

config("MONGODB_URI")

returns

mongodb://localhost:27017/blog
Step 3: Pass it to MongoEngine
connect(
    host=config("MONGODB_URI")
)

becomes

connect(
    host="mongodb://localhost:27017/blog"
)

MongoEngine then connects to that MongoDB instance.

What if .env doesn't have MONGODB_URI?

Your code has a default value:

config(
    "MONGODB_URI",
    default="mongodb://localhost:27017/blog_platform"
)

So if the variable is missing,

# .env
# MONGODB_URI is not present

then

config("MONGODB_URI", default="mongodb://localhost:27017/blog_platform")

returns

mongodb://localhost:27017/blog_platform

instead.

Complete flow
.env
─────────────────────────────
MONGODB_URI=mongodb://localhost:27017/blog
            │
            ▼
core/database.py
─────────────────────────────
config("MONGODB_URI")
            │
            ▼
Returns:
"mongodb://localhost:27017/blog"
            │
            ▼
connect(host="mongodb://localhost:27017/blog")
            │
            ▼
MongoEngine connects to MongoDB
Why use an environment variable?

Instead of hardcoding:

connect(host="mongodb://localhost:27017/blog")

you use:

connect(host=config("MONGODB_URI"))

This allows you to change the database connection without modifying your source code:

Local development: mongodb://localhost:27017/blog
Testing: mongodb://localhost:27017/test_blog
Production/Atlas: mongodb+srv://...
