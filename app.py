
import os
import random

import discord
from discord.ext import commands


###################################################
#                 SETTINGS
###################################################

bot = commands.Bot(command_prefix='#')


###################################################
#                 HELPERS
###################################################

def split_groups(members):
    groups = []

    if len(members) % 2 == 0:
        while len(members) > 0:
            duet = random.sample(members, 2) # get 2-members list
            groups.append(duet) # add new group to output list

            # remove them from input list
            members.remove(duet[0])
            members.remove(duet[1])
    else:
        while len(members) > 1: # last member left
            duet = random.sample(members, 2)
            groups.append(duet)
            members.remove(duet[0])
            members.remove(duet[1])
        groups[-1].append(members[0]) # add last member to last list

    return groups


###################################################
#                 DISCORD
###################################################

async def create_channels(ctx, num):
    current_channels_dict = { c.name: c for c in ctx.guild.voice_channels } # { channel_name: channel_object, ...}
    current_channels_names = current_channels_dict.keys()

    output_channels = []
    for i in range(num):
        channel_name = "Talk Time #{}".format(str(i+1))

        # if channel_name not exists then create
        if channel_name not in current_channels_names:
            # create new channel
            try:
                print("Create channel:", channel_name)
                new_channel = await ctx.guild.create_voice_channel(channel_name)
            except:
                print("Creating voice channel error!!!")
                exit(1)
        else:
            # get channel from dict
            new_channel = current_channels_dict[channel_name]

        # add to output list
        output_channels.append(new_channel)

    return output_channels


@bot.listen()
async def on_ready():
    print('My name is: {0.user}\n'.format(bot))


@bot.command(name='talk-time-echo')
async def hello(ctx, arg):
    await ctx.send(arg)


@bot.command(name='talk-time-start')
async def start_talk_time(ctx):

    members = ctx.message.mentions # get members from mentions in command -> #talk-time-start @member1 @member2 ...
    if len(members) < 2:
        await ctx.send("Not enough members. I need at least 4")
        return

    required_channels = len(members) // 2 # 2 members per one channel (if odd then one channel will contain 3 members)

    groups = split_groups(members) # create 2 person groups

    channels = await create_channels(ctx, required_channels)

    # divide into groups
    for group, channel in zip(groups, channels):
        print("Group: \n\t{} => Channel: {}".format(' '.join([i.name for i in group]), channel))
        for member in group:
            try:
                print("Move {} to {}".format(member, channel))
                await member.move_to(channel)
            except:
                print("Moving error!!!")
                exit(1)

    await ctx.send("Talk Time started!")


###################################################
#                 MAIN
###################################################

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
