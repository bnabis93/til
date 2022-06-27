# Github action
- GitHub Actions `workflow` to be triggered when an event occurs in your repository (e.g. event : PR, commit, merger, ...)
- Your workflow contains one or more jobs which can run in sequential order or in parallel. 
- Each job will run inside its own virtual machine runner (runner라는 VM)

## Workflow
- Automated process that will run one or more jobs
- Repository can have multiple workflows
- 예를 들어 commit에 대한 workflow, PR에 대한 workflow, deploy시의 workflow 등등

## Event
- Github action은 github event에 trigger되어 workflow의 job을 실행시킨다.
- event의 예시로써는 PR을 만든다던지, PR을 올린다던지, commit을 올린다던지, 등등 github에서 발생할 수 있는 대부분의 event.
- event 확인 -> (ref)[https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows]


## Jobs
- Set of steps in a workflow that execute on the same runner.
- 하나의 runner (VM)에서 실행되는 step들의 집합이 job이다.
    - 여기서 step은 shell script 혹은 실행되는 작업을 의미한다.
    - 즉, 하나의 VM에서 shell script 혹은 실행되는 작업들의 집합이 job이다.
    - 각 step은 순차적으로 실행된다. 
    - step, 같은 VM에서 실행되고 있다면, 자원공유가능
- 기본적으로 job들간의 종속성은 없고, 각 job들은 병렬적으로 실행 됨 (step과 job을 구분할것, job은 step으로 이루어진것)
- 종속성이 생길수도 있는데 이러면 인과관계 (A job 이후에 B job이 실행된다.) 가 생긴다. (순차적)

## Actions
- https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
- An action is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task.
- 좀 복잡하한데 자주쓰이는 task들을 미리 정의해놓은듯, (보니까 `step`의 `uses` 에서 사용되는듯)

## Runner
- 실제 job들이 (workflow가) 실행 될 물리적인 서버를 의미함
- git의 서버를 사용할수도, 본인이 가진 서버를 사용 할 수도 있다.(self-hosted runner)


## Understanding the workflow file
- `name` : workflow 이름 (optional)
- `on` : Specifies the trigger for this workflow. (어떤 event에 대한 trigger)
- `runs-on` : 어떤 runner에서 돌릴거냐
- `uses` in step : 해당 레포를 runner에게 checkout 하여 실제 runner에서 실행되는 부분, action~ 으로 정의된것은 뭐지
- `run` : runner의 커멘드에서 실행