### Git笔记

##### 什么是git?

> Git是目前世界上最先进的分布式版本控制系统（没有之一）。



##### 仓库初始化

进入到某个目录下, 输入以下命令,即可将该目录变成Git可以管理的仓库

```shell
git init
```

PS:所有的版本控制软件都只能跟踪文本文件的改动, 但是像图片,视频,word等二进制文件,Git无法直接跟踪其文件变化.



##### 把一个文件添加到Git 仓库

1. Add

   ```shell
   git add <文件名>
   ```

2. commit

   ```shell
   git commit <文件名> -m "<本次提交的说明>"
   ```



##### 查看当前仓库状态

```shell
git status
```

该命令可以看到当前哪些文件继上一次提交后又被修改过,但仍未提交的



##### 查看修改的内容

```shell
git diff [HEAD -- <文件名>]
```



##### 提交修改的文件

1. add
2. commit

和添加一个文件到Git仓库的步骤是一样的



##### 撤销修改

```shell
git checkout -- <文件名>
```

该命令可以将工作区的文件的修改丢弃掉, 它会让文件会到最近一次`git commit`或者`git add`时的状态



##### 查看历史提交记录

```shell
git log
```

如果嫌输出信息太多，看得眼花缭乱的，可以试试加上`--pretty=oneline`参数



##### 版本回退

###### 回退到上一个版本

```shell
git reset --hard HEAD^
```

###### 回退到上上个版本

```shell
git reset --hard HEAD^^
```

...

###### 回退到n个版本前

```shell
git reset --hard HEAD~n
```

###### 回退到指定版本

```shell
git reset --hard <commitid>
```

`commitid`可以从`git log`中找到



##### 获取你的每一次命令

```shell
git reflog
```



##### 暂存区

> stage(index), 文件`git add`后就被git加入了暂存区, `git commit`后文件会被移出到master分支中.

![git-repo](0.jpg)

- 只有被加入了stage中的文件或修改, 才能进一步的commit到master分支中



##### 撤回暂存区中的修改

对于已经`git add`的修改来说, 它们已经被添加到了暂存区, 可以用以下命令来撤回

```shell
git reset HEAD <文件名>
```

撤回后, 可以用`git checkout -- <文件名>`来撤销工作区文件的修改



##### 删除文件

当你删除掉某文件后, (手动删除掉文件/`rm <文件名>`), 会存在两种情况.一种是因为失误删除掉, 所以需要从版本库中恢复, 另一种情况是确实要删除, 需要将版本库中的该文件一并删除

###### 删除版本库中的文件

1. `git rm <文件名>`

2. `git commit`

###### 恢复工作区中被删除的文件

```shell
git checkout -- <文件名>
```



##### 远程仓库

- 关联一个远程仓库

  ```shell
  git remote add origin <远程git地址>
  ```

- 第一次推送master分支所有内容

  ```shell
  git push -u origin master
  ```

- 此后的提交

  ```shell
  git push origin master
  ```



##### 克隆一个远程仓库

进入一个目录, 然后运行一下命令

```shell
git clone <gitURL>
```

`gitURL`一般是一个网址,以`.git`结尾



##### 分支

###### 什么是分支

> 分支就是科幻电影里面的平行宇宙，当你正在电脑前努力学习Git的时候，另一个你正在另一个平行宇宙里努力学习SVN。
>
> 如果两个平行宇宙互不干扰，那对现在的你也没啥影响。不过，在某个时间点，两个平行宇宙合并了，结果，你既学会了Git又学会了SVN！
>
> 分支在实际中有什么用呢？假设你准备开发一个新功能，但是需要两周才能完成，第一周你写了50%的代码，如果立刻提交，由于代码还没写完，不完整的代码库会导致别人不能干活了。如果等代码全部写完再一次提交，又存在丢失每天进度的巨大风险。
>
> 现在有了分支，就不用怕了。你创建了一个属于你自己的分支，别人看不到，还继续在原来的分支上正常工作，而你在自己的分支上干活，想提交就提交，直到开发完毕后，再一次性合并到原来的分支上，这样，既安全，又不影响别人工作。



###### HEAD

指向Git中的主分支master(指向提交)

![git-br-initial](1.jpg)

###### 创建分支

```shell
git branch <分支名>
```



###### 切换分支

```shell
git checkout <分支名>
```

新版本也可以使用如下命令

```shell
git switch <分支名>
```



###### 创建并切换分支

```shell
git checkout -b <分支名>
```

新版本也可以使用如下命令

```shell
git switch -c <分支名>
```



###### 查看当前分支

```shell
git branch
```

该命令会列出所有的分支, 当前分支前面会标有一个`*`号



###### 合并分支

```shell
git merge <分支名>
```

将指定的分支合并到当前分支



##### 删除分支

```shell
git branch -d <分支名>
```

当要删除的分支有修改没有被合并时, 无法直接删除,如果要强制删除, 可以使用:

```shell
git branch -D <分支名>
```



##### 解决冲突

当Git无法自动合并时, 就必须首先解决冲突, 解决冲突后, 再提交, 然后完成合并.

**解决冲突**:把Git合并失败的文件手动编辑为我们希望的文件内容, 再提交.

###### 查看分支合并图

```shell
git log --graph
```



##### 不使用`fast-forward`方式合并

- 什么是`fast-forward`方式合并: 直接将"当前分支指针"指向要合并的分支, 使用`git merge`时默认使用的就是该方式

那么,如何不使用`fast-forward`方式合并呢?

```shell
git merge --no-ff -m "<合并提交信息>" <分支名>
```

例如:

```shell
git merge --no-ff -m "merge with no-ff" dev
```

表示, 将`dev`分支合并到当前分支(`master`)

这样合并后有历史, 可以看出曾经做过合并, 而`fast forward`模式看不出来曾经合并过.



##### 分支策略

- `master`分支: 应该稳定, 仅仅用来发布新版本
- `dev`分支: 不稳定, 平时更新自己修改的部分内容时使用
- 团队协作时, 应该还有自己的独立分支: 提交自己的修改, 完成一个任务时, 合并到`dev`中去. 



##### 隐藏修改(保存工作现场)

- 隐藏修改

  ```shell
  git stash
  ```

- 查看隐藏列表

  ```shell
  git stash list
  ```

- 恢复隐藏(恢复工作现场)

  恢复的同时把`stash`内容删除

  ```shell
  git stash pop
  ```

  恢复`stash`

  ```shell
  git stash apply [<stassh名称>]
  ```

  `stassh`名称可以用`git stash list`查看, `:`前的即为`stash`名称

  删除`stash`

  ```shell
  git stash
  ```

  

##### 复制一个特定的提交到当前分支

```shell
git cherry-pick <commitId>
```

如果这个提交会造成冲突(`error: Your local changes to the following files would be overwritten by merge`):

1. `git stash`: 隐藏当前的工作空间
2. `git cherry-pick <commitId>`: 这时候再合并那个特定的提交
3. `git stash pop`: 恢复`stash`
4. 解决冲突
5. `git add <file>`
6. `git commit -m "<commit message>"`

例子可以参考这篇文章中描述的问题:

[Bug分支]: https://www.liaoxuefeng.com/wiki/896043488029600/900388704535136



##### 查看远程库的信息

```shell
git remote [-v]
```



##### 推送分支

```shell
git push origin <分支名>
```



##### 抓取分支

```shell
git pull
```

一般情况下, 你`clone`一个仓库后, 是只能看到`master`分支的, 因此需要本地建立一个同名分支, 并和远程分支关联:

1. 创建本地分支, 与远程分支关联(**适用于本地未建立,而远程建立的某分支**)

   ```
   git checkout -b <分支名> origin/<分支名>
   ```

2. 指定本地分支与远程分支的链接(**适用于本地以建立, 但是还未和远程建立关联**)

   ```shell
   git branch --set-upstream-to=origin/<分支名> <分支名>
   ```

3. 此时重新拉取

   ```shell
   git pull
   ```

   

##### 整理提交历史

```shell
git rebase
```

> - rebase操作可以把本地未push的分叉提交历史整理成直线；
> - rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。



##### 标签

###### 什么是标签?

> Git的标签是版本库的快照，其实它就是指向某个`commit`的指针（跟分支很像对不对？但是分支可以移动，标签不能移动）
>
> tag就是一个让人容易记住的有意义的名字，它跟某个`commit`绑在一起。
>
> - PS: 标签总是和某个`commit` 挂钩, 如果某个`commit`在多个分支出现, 那么在多个分支上都可以看见该标签

###### 创建标签

切换到你要打标签的分支

```shell
git tag <标签名> [<commitId>]
```

如:`git tag v1.0`

- 不指定`commitId`则表示对当前分支的最新的提交打标签

- 指定了`commitId`则表示对指定的提交打标签

*还可以创建带有说明的标签

```shell
git tag -a <标签名> -m "<说明>" <commitId>
```

###### 查看标签信息

```shell
git show <标签名>
```



##### 删除标签

###### 删除本地标签

```shell
git tag -d <标签名>
```

###### 删除远程标签

```shell
git push origin :refs/tags/<标签名>
```



##### 推送标签

###### 推送一个本地标签

```shell
git push origin <标签名>
```

###### 推送全部未推送过的本地标签

```shell
git push origin --tags
```



##### `.gitignore`文件

> `gitignore`文件中保存着Git应该忽略的文件名/规则

忽略文件的原则是：

1. 忽略操作系统自动生成的文件，比如缩略图等；
2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的`.class`文件；
3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

`github`官方给出了一些模板:[.gitignore模板](https://github.com/github/gitignore)

强制添加一个文件到Git

```shell
git add -f <file>
```

检查`.gitignore`哪条规则忽略了某文件

```shell
git check-ignore -v <file>
```



##### 配置别名

```shell
git config [--global] alias.<别名> <原名>
```

例如: `git config --global alias.st status` 表示以后`st`就表示`status`

- 加了`--global` 表示针对全局有效, 不加则表示针对当前仓库有效

###### 配置文件

1. 全局配置文件

   位于用户主目录下的一个`.gitconfig`文件中, 可以在其中添加如下代码配置全局别名:

   ```
   [alias]
       co = checkout
       ci = commit
       br = branch
       st = status
   ```

2. 当前仓库的配置文件位于`./.git/config` , 同样可以通过以上代码直接配置当前仓库的别名.