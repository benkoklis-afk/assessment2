[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Rqple_X8)
# Individual CI project

  
## Description

You are in a team about to start the development of a web-application and you wish to create all
the necessary infrastructure for supporting CI/CD.

This repository contains some requirements, that aim to test your skills on git, git best practices, git
flow, Github actions, Docker and Heroku. You should tread lightly from step to step to avoid tricky situations. 
Following the guidelines discussed in class you should be able to deliver all the requirements and handle all the various situations presented.

You are required to use Github Projects for the coordination and management of all the requirements. 


* Follow [this](https://chris.beams.io/posts/git-commit/) guide for writing git commit messages
except if you are asked otherwise.
* Local & remote branches should be in sync at all times.
* Every feature should land on a new branch.
* Every PR should adhere to the Pull request guidelines.
* Whenever a PR is successfully reviewed and can be merged you should proceed with the merging unless otherwise instructed.
* Every requirement related to the repository should belong to a unique issue on Github.
* Commits should contain references on Github issues according to the git commit message best practices referenced earlier.
* Whenever you are not asked to create a specific type branch you should evaluate the situation and decide which type of branch suits the specific case.
* You are responsible for having accurate branch types according to git-flow.
* New features should never break the develop branch. Merging a branch with a broken build on develop would be penalised. The same applies to the master.

## PLANNING PHASE
* By heading to your repository there is a tab next to `Actions` which is named `Projects`. Create a new project using the `Board` template.
* Link the new project to the repo project and activate the default workflows.
* Create a pull request template for your repository
* Create Issue templates for bugs & features for your repository
* Enable Dependency graph on Github settings
* Enable Dependabot alerts
* Enable Dependabot security updates
* Create branch protection rules for your master & develop branch adhering to the following: `Require status checks to pass before merging`, `Do not allow bypassing the above settings`. In case you would like to add extra rules for additional branches and you believe that you will benefit from this please feel free to do so.

### General Guidelines
* You are responsible for identifying/extracting issues from the following requirements. 
Grouping features together needs to be accompanied by appropriate justification. 
Grouping unrelated work on a feature will be penalised.

* All issues should be created on the project board **prior to starting anything**. 
You should take some time and locate every single issue. Issues not related directly with the git repository should be created as a note on the project board. Everything needs to be in place before you start working on any requirements apart from the first one which actually creates the Project board.

### Requirements:
You are supplied with a python project that you will have to onboard to the repository. This project is located in the github repo in the `battlesnakes` folder and it is an HTTP server that provides multiple webhooks that are accessed from a [game server](https://play.battlesnake.com/). Your aim is to create a development pipeline that will support continuous integration features from the moment a developer is making project changes, to the delivery of the software to the end customer. In other words, from code building to Heroku deployments and from code testing to application performance monitoring.

Your first step is to create a workflow that will allow for the continuous build and test of the code base. You should put your skills in action and use what we learned during class in order to create a multistep build process that will check and enforce coding standards throughout the project development lifecycle. Don’t forget to include a linting step where you will check for the formatting of the python project using the `flake8` checker. 

The pipeline should break if the project is not following the default flake8 rules with the exception of the max-line-size which can be set to 110. You can use `black` to format the codebase in order to pass the checks. 

This is a good point to provide a beta version as the release of your codebase.

Once you have successfully created the build and test workflows. You should proceed with integrating external services in order to effectively alert the involved parties and stakeholders. The output of the pipeline should be sent to a slack channel that will be provided to you. A simple shell script similar to the one we saw on github actions workshop (step 3), should do the trick. Don’t forget to safely store your secrets (like webhook tokens) to your repository otherwise you are risking the possibility of getting blocked by slack’s intelligent public repo scanner. 

Next, you will need a dockerfile and a relevant docker compose file that will house the Python HTTP server. 

Using `alpine` as base, create a dockerfile that will install `python3`. Don't forget to move any relevant files/folder into your docker image and keep in mind that you will need to install `pip` in order to manage the dependencies from the requirements file. You can install pip using:

```
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 ./get-pip.py
```

Once your dockerfile is ready, you should follow with an automated step that will create and push your docker image to your dockerhub repository. This image should be public and accessible from anywhere in the world. 

Don't forget to make a proper release version now that you have the containers in place.

Once you are happy with the containerization of the project, your final stage is the deployment and monitoring of the live system. For that purpose, you will have to create a Heroku deployment workflow that will push your project to a free heroku dyno. Don’t forget to add me as a collaborator to your heroku application.

And for the final part that will be the final feature of this project you will have to integrate your heroku application with datadog for application performance monitoring and alerting. 

In order to do that, you need to create a free account on [Datadog](https://app.datadoghq.eu/). 
Then, you will have to set heroku to push the generated log files to datadog using the the [heroku's log drains](https://docs.datadoghq.com/logs/guide/collect-heroku-logs/).
And finally create an [integration](https://app.datadoghq.eu/account/settings#integrations/webhooks) with the existing webhook for your slack `Alerts` channel.
Note: You will have to create a custom payload for your integration.

Once everything is setup, you will need to create a [new monitor](https://app.datadoghq.eu/monitors#/create).
for your logs in order to send alerts for 404 requests using the slack integration that you created before.



## Useful links
- https://devcenter.heroku.com/articles/how-heroku-works
- https://devcenter.heroku.com/categories/deployment
- https://help.github.com/en/actions/automating-your-workflow-with-github-actions/workflow-syntax-for-github-actions
- https://github.com/marketplace?type=actions
- https://github.com/settings/tokens
- https://medium.com/@hugooodias/the-anatomy-of-a-perfect-pull-request-567382bb6067
- https://help.github.com/en/github/administering-a-repository/about-protected-branches
- https://app.datadoghq.eu/
- https://docs.datadoghq.com/logs/guide/collect-heroku-logs/
- https://devcenter.heroku.com/articles/log-drains
- https://docs.datadoghq.com/integrations/webhooks/
- https://app.datadoghq.eu/monitors#/create
