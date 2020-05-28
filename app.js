const Discord = require('discord.js');
const client = new Discord.Client();
const request = require('request-promise');
const fs = require('fs');
const config = JSON.parse(fs.readFileSync(__dirname+'/config.json'));
const accessToken = config.token;
const target = config.target;
const options = {
    url: 'https://bonychops.com/experiment/discord-police/api/getGoglerPoint.php',
    method: 'GET',
    json: true
}

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', async(msg) => {
  if (msg.content === '/get point') {
    if(msg.guild.members.cache.find(member => member.user.id == target).user.presence.status != "online"){
        msg.channel.send("```※TEST Botがオフラインであるため、非公式botがお送りいたします。\n非公式のため動作が安定しない可能性があります。```");
        request(options, function (error, response, body) {
            if(error){
                msg.channel.send("```えらったw\n※所詮は非公式なんすね```");
            }else{
                Object.keys(body.data).forEach(async(user) => {
                    await msg.channel.send(`${body.data[user].name}は現在${body.data[user].point}ptです。`);
                })
            }
        })
    }else{
        console.log("Official bot is online now");
    }
  }
});

client.login(accessToken);