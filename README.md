# Talk Time Discord bot

Connect people by creating voice channels with two-person groups.


# Best for

- team/group integration
- speed dating
- discussion meetings

## How to use it?

1. Add bot to your channel
2. Get the people together on **some** voice channel (minimum 4 persons)

   `Every person should be IN some voice channel`
3. Type a command:
   ```
    #talk-time-start @person1 @person2 @person3 @person4 .....
   ```
   Mention every person that take part in event.

Bot will create necessary voice channels and divide people into 2-person groups in this channels.

In case of odd number of people, the last group will have 3 persons.


## How to run app? - Docker Way

1. Provide DISCORD_TOKEN in `.env` file
2. Run: `make build`
3. Run: `make run`

