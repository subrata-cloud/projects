$(document).ready(function(){
    $('#repoWrapper').hide();
    $('#topicWrapper').hide();
});

async function getUserDetails(){
    const user=document.getElementById('user');
    if(user.value!='')
    {
        const msg=document.getElementById('errorMsg');
        msg.style.color="";
        msg.innerHTML="";
        user.style.border=""; 
        const url=`https://api.github.com/users/${user.value}`;
        const response=await fetch(url,{
            method: "get",
            header:{"Authorization":"Basic subrata-cloud:subrata.git@19"}

        });
        const user_details= await response.json();
        showUser(user_details);     
        getRepos(user_details.repos_url);

    }
    else
    {
        const msg=document.getElementById('errorMsg');
        msg.style.color="red";
        msg.innerHTML="Git username is required";
        user.style.border="2px solid red";
    }
}

async function showUser(user_details){
    const userParent=document.getElementById('userParent');
    const avatarImg=document.createElement('img');
    const repoSpan=document.getElementById('repoSpan');
    const followersSpan=document.getElementById('followersSpan');
    const followingSpan=document.getElementById('followingSpan');
    repoSpan.innerHTML=user_details.public_repos;
    followersSpan.innerHTML=user_details.followers;
    followingSpan.innerHTML=user_details.following;
    avatarImg.src=user_details.avatar_url;
    avatarImg.setAttribute("width","100%");
    avatarImg.setAttribute("height","250px");
    userParent.appendChild(avatarImg);
    const nameP=document.createElement('p');
    nameP.innerHTML=user_details.login;
    nameP.style.marginTop="10px";
    nameP.style.fontSize="20px";
    nameP.style.color="rgb(173, 167, 167)";
    userParent.appendChild(nameP);
    $('#repoWrapper').show();
}

async function getRepos(user_details){
    const user_repos = await fetch(user_details,{
        method: "get",
        header:{"Authorization":"token ecf14416a499b4139272cf1ef5ac4be0253758a8"}
    });
    const repo_list = await user_repos.json();
    showRepos(repo_list);
}

async function showRepos(repo_list){
    const repoParent=document.getElementById('repoParent');
    for(let repo=0;repo<repo_list.length;repo++)
    {
        const childWrapper=document.createElement('div');
        const repoChild=document.createElement('span');
        repoChild.setAttribute('onclick',`getTopics('${repo_list[repo].url}')`);    
        repoChild.innerHTML=repo_list[repo].name;
        repoChild.style.color="blue";
        childWrapper.appendChild(repoChild);
        repoParent.appendChild(childWrapper);
    }
    $('#repoWrapper').show();
}

async function getTopics(repo_url){
    const topics_response = await fetch(repo_url,{
        method: 'get',
        headers: {
            "Accept":"application/vnd.github.mercy-preview+json",
            "Authorization":"token ecf14416a499b4139272cf1ef5ac4be0253758a8"
        }
    });
    const topics_list =  await topics_response.json();
    showTopics(topics_list);
} 

async function showTopics(topics_list){
    const topicParent=document.getElementById('topicParent');
    const btnTopic=document.getElementById('btnTopic');
    const ownerRepo=document.getElementById('ownerRepo');
    ownerRepo.innerHTML=topics_list.full_name;
    btnTopic.setAttribute('onclick',`prepareAddTopic('${topics_list.url}')`);
    if(topicParent.hasChildNodes)
    {
        topicParent.innerHTML='';
        localStorage.removeItem('topics');
    }
    for(let topic=0;topic<topics_list.topics.length;topic++)
    {
        const topicP=document.createElement('p');
        topicP.innerHTML=topics_list.topics[topic];
        topicP.style.color="black";
        topicP.style.fontSize="16px";
        topicP.style.width="100%";
        const topicSpan=document.createElement('span');
        topicSpan.innerHTML="Delete";
        topicSpan.setAttribute('onclick',`prepareDeleteTopic('${topics_list.url}','${topics_list.topics[topic]}')`);
        topicSpan.className="btn btn-danger";
        topicSpan.style.float="right";
        topicSpan.style.color="white";
        topicSpan.style.fontSize="16px";
        topicP.appendChild(topicSpan);
        topicParent.appendChild(topicP);
    }
    localStorage.setItem('topics',topics_list.topics);
    $('#topicWrapper').show();
}

async function prepareAddTopic(repo_url)
{
    const topic=document.getElementById('topic');
    const topicMsg=document.getElementById('topicErrorMsg');
    var topics=localStorage.getItem('topics');
    if(topics !='')
        topics=topics.split(',');
    else
        topics=[];
    if (topic.value!='')
    {
        topicMsg.style.color="";
        topicMsg.innerHTML="";
        topic.style.border=""; 
        topics.push(topic.value);
        topic.value='';
        addUpdatedTopics(repo_url,topics);
    }
    else
    {
        topicMsg.style.color="red";
        topicMsg.innerHTML="Topic name required.";
        topic.style.border="1px solid red";
    }
}

async function prepareDeleteTopic(repo_url,topic){
    if(confirm('Are you sure to delete this topic?'))
    {
        var topics=localStorage.getItem('topics');
        topics=topics.split(',');
        for(let index=0; index< topics.length;index++)
         {
            if (topics[index]==topic)
               topics.splice(index,1);
        }
        addUpdatedTopics(repo_url,topics);
    }
}

async function addUpdatedTopics(repo_url,topics)
{
    const topics_response = await fetch(repo_url+'/topics',{
        method:"put",
        headers: {
            "Accept":"application/vnd.github.mercy-preview+json",
            "Authorization":"token ecf14416a499b4139272cf1ef5ac4be0253758a8"            
        },
        body:JSON.stringify({"names":topics})
    });
    const topics_list =  await topics_response.json();
    showUpdatedTopics(repo_url,topics_list);

}

async function showUpdatedTopics(repo_url,topics_list){
    const topicParent=document.getElementById('topicParent');
    const btnTopic=document.getElementById('btnTopic');
    btnTopic.setAttribute('onclick',`prepareAddTopic('${repo_url}')`);
    if(topicParent.hasChildNodes)
    {
        topicParent.innerHTML='';
        localStorage.removeItem('topics');
    }
    for(let topic=0;topic<topics_list.names.length;topic++)
    {
        const topicP=document.createElement('p');
        topicP.innerHTML=topics_list.names[topic];
        topicP.style.color="black";
        topicP.style.fontSize="16px";
        topicP.style.width="100%";
        const topicSpan=document.createElement('span');
        topicSpan.innerHTML="Delete";
        topicSpan.setAttribute('onclick',`prepareDeleteTopic('${repo_url}','${topics_list.names[topic]}')`);
        topicSpan.className="btn btn-danger";
        topicSpan.style.float="right";
        topicSpan.style.color="white";
        topicSpan.style.fontSize="16px";
        topicP.appendChild(topicSpan);
        topicParent.appendChild(topicP);
    }
    localStorage.setItem('topics',topics_list.names);
    $('#topicWrapper').show();
}