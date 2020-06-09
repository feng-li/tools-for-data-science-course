Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request import urlopen
>>> from bs4 import BeautifulSoup
>>> html = urlopen('https://www.thepaper.cn/newsDetail_forward_7758236')
>>> bs = BeautifulSoup(html.read(), 'html.parser')
>>> nameList=bs.findAll('div',{'class':'newscontent'})
>>> for name in nameList:
	print(name.get_text())

	


澎湃号 > 双鸭山公安

新冠疫苗优先为谁接种？权威回应！


2020-06-08 20:45 来源：澎湃新闻·澎湃号·政务

字号

超大
大
标准
小









双鸭山公安


关注




7日，国务院新闻办公室发布《抗击新冠肺炎疫情的中国行动》白皮书。发布会上，相关部门负责人介绍了白皮书有关情况并答记者问。1.中国研制出新冠疫苗后先为谁接种？科技部部长王志刚：疫苗研发难度大、周期长，具有很大的不确定性，中方疫苗研制过程注重加强国际合作。到了应用的时候，我们会践行承诺，把它作为全球公共产品，向人类提供。2.如何提高疾控中心的地位？国家卫健委主任马晓伟：要明确国家CDC（疾控中心）、省级CDC、市县级CDC各自的功能定位。国家CDC要解决科研研发、实验室检测、业务指导和病原学分析等“一锤定音”的能力；省级CDC要发挥区域防控工作的指导、监督、质量评估和人才培养方面的作用；市县级CDC要进一步加强现场流行病学的调查和对地区性传染病疾病谱的日常监管和监测。此外，下一步将完善网络疫情直报系统和突发公共卫生事件行政报告系统。3.中国媒体在打“信息战”？国新办主任徐麟：疫情发生以来，480名中国媒体人逆行出征，令人尊敬。中国媒体关于抗疫的报道是实事求是、真实客观的，指责中国媒体进行所谓的虚假宣传是枉顾事实，完全站不住脚的。中国媒体无意打所谓的“信息战”，但是面对对中国的造谣诬蔑和攻击抹黑，中国媒体必须、也必然会做出回应。这种回应不是打嘴仗，而是正本清源、明辨是非。病毒是人类共同的敌人，虚假信息也是人类共同的敌人。媒体应该展现责任担当，中国媒体已经在这么做，还将继续做下去。4.中国哪些治疗经验可与国际社会分享？国家卫健委主任马晓伟：在控制病源、加强检测、进行大规模医疗救援、发挥中医中药作用等方面，都值得认真总结和借鉴。5.如何恢复国际人员交往？外交部副部长马朝旭：正逐步有序恢复中外人员往来，服务于复工复产。中方已和韩国、德国、新加坡等一些国家建立“快捷通道”，目前运转顺利。6.中国和别国的关系是否受疫情冲击而变差？外交部副部长马朝旭：不认同这种说法。事实是，我们的朋友更“铁”了，中国的“朋友圈”更大了。3月1日至5月31日，中国出口口罩706亿只，出口防护服3.4亿件，这些都体现了中国负责任大国的担当，也促进了和各国关系的发展。7.会否和外国专家合作追溯病毒起源？科技部部长王志刚：坚持依靠科学家、坚持科学态度、运用科学方法做好溯源工作。8.中国延误一周公布数据导致疫情扩散？国家卫健委主任马晓伟：不同意这种说法。事实是中国政府没有任何延误和隐瞒。新冠病毒是前所未有的新病毒，人类对它的认识存在大量的未知，这里有一个证据逐渐积累、认识不断深化的过程。9.中国民众在抗疫中发挥了什么作用？国新办主任徐麟：在中国，党和政府与人民是血肉相连的整体。人民的主体作用，在抗击疫情的过程中表现非常充分。武汉有位90后女青年，不幸一家三口都患上新冠肺炎，其父医治无效去世。女孩一边自己坚持治疗，一边每天登录父亲的微信，以父亲的口吻和母亲保持联系，鼓励母亲要坚持，最终母女痊愈。一位来自湖南长沙的90后小伙，在武汉实施离汉通道管制后，辞别亲友驾私家车来到武汉，为医务工作者提供服务，成为“最美摆渡人”。这两位90后年轻人就是14亿中国人民的缩影，14亿中国人民都是抗击疫情的伟大战士。10.中国还有什么计划继续深化抗疫国际合作？外交部副部长马朝旭：中国宣布的合作措施都在落实。关于中国将提供20亿美元的援助，既包括提供抗疫物资援助，也包括支持有关国家疫后的经济社会恢复和发展；既包括双边援助也包括多边捐赠。此外，关于联合国人道主义应急仓库和枢纽在中国建设，这件事正在商谈和加紧筹建中。11.中国新冠治疗药物研发进展如何？会否向国外推荐和推广？科技部部长王志刚：我们现在正在研究抗体性药物，现在第一个抗体药已经通过药监局的评审。中方向200多个国家和地区分享了科研成果，各国根据自身情况进行选择。原标题：《新冠疫苗优先为谁接种？权威回应！》阅读原文





 发送邮件至zhengwu@thepaper.cn申请加入澎湃政务号或媒体团
特别声明本文为政务等机构在澎湃新闻上传并发布，仅代表该机构观点，不代表澎湃新闻的观点或立场，澎湃新闻仅提供信息发布平台。




0

收藏








评论（0）




>>> 
