#!/usr/bin/env python
# encoding: utf-8
"""
@author: youfeng
@email: youfeng243@163.com
@license: Apache Licence
@file: company_list.py
@time: 2017/7/4 11:40
"""

data_list = ["湖南金隅阳光投资有限公司",
             "黔张常铁路有限责任公司",
             "衡茶吉铁路有限责任公司",
             "石长铁路有限责任公司",
             "湖南基础建设投资集团有限公司",
             "怀邵衡铁路有限责任公司",
             "湖南基础建设保险代理有限公司",
             "湖南磁浮交通发展股份有限公司",
             "沪昆铁路客运专线湖南有限责任公司",
             "蒙西华中铁路股份有限公司",
             "湖南湘铁集团铁路建设有限公司",
             "湖南炎帝资产管理有限公司",
             "长沙湘江新城投资有限公司",
             "长沙先导城市建设投资有限公司",
             "长沙先导物业管理有限公司",
             "长沙市滨江新城建设开发有限责任公司",
             "湖南空港实业股份有限公司",
             "长沙先导产业投资有限公司",
             "长沙先导恒伟房地产开发有限公司",
             "长沙综合交通枢纽建设投资有限公司",
             "长沙先导酒店投资管理有限公司",
             "长沙先导恒通商业管理有限公司",
             "长沙月亮岛文旅新城投资有限公司",
             "长沙先导资产经营管理有限公司",
             "吉祥人寿保险股份有限公司",
             "长沙先导文化旅游投资有限公司",
             "长沙先导洋湖建设投资有限公司",
             "湖南湘江新区先导滨江私募基金发展合伙企业（有限合伙）",
             "长沙先导投资管理有限公司",
             "湖南乾瑞航空产业投资管理有限公司",
             "长沙市信息基础设施建设投资发展有限公司",
             "长沙月亮岛美猴王国投资有限公司",
             "长沙先导智慧城市投资有限公司",
             "长沙先导建筑材料有限公司",
             "长沙先导梅溪湖建设投资有限公司",
             "湖南发展资产管理集团有限公司",
             "湖南金隅阳光投资有限公司",
             "湖南发展集团资本经营有限公司",
             "湖南发展高新置业有限公司",
             "湖南城际铁路有限公司",
             "湖南悦达发展投资有限公司",
             "湖南华菱钢铁集团有限责任公司",
             "湖南省棚户区改造投资有限公司",
             "汨罗国开村镇银行股份有限公司",
             "湖南省扶贫开发投资有限公司",
             "湖南发展集团土地储备开发有限公司",
             "湖南省包装集团有限公司",
             "华菱控股集团有限公司",
             "湖南发展集团国有资产管理有限公司",
             "泰格林纸集团股份有限公司",
             "湖南发展集团矿业开发有限公司",
             "湖南发展集团九华城市建设投资有限公司",
             "湖南省保障性安居工程投资有限公司",
             "开元发展（湖南）基金管理有限责任公司",
             "湖南湖湘商贸股份有限公司",
             "国开发展湖南两型元盛基金企业（有限合伙）",
             "吉祥人寿保险股份有限公司",
             "长沙市土地开发建设有限责任公司",
             "湖南水口山有色金属集团有限公司",
             "湖南有色集团湘东钨业有限公司",
             "湖南有色湘乡氟化学有限公司",
             "内蒙古金湘矿业有限责任公司",
             "湖南有色置业发展有限公司",
             "郴州柿竹园实业有限责任公司",
             "湖南有色南岭资源开发有限公司",
             "吉林东北有色金属有限公司",
             "湖南有色中央研究院有限公司",
             "汪清自硬钨钼材料有限公司",
             "湖南湘铝有限责任公司",
             "湖南有色新材料科技有限公司",
             "株洲冶炼集团股份有限公司",
             "湖南有色金属投资有限公司",
             "冷水江锡矿山有色实业有限责任公司",
             "长沙矿山研究院有限责任公司",
             "五矿稀土江华有限公司",
             "湖南海斯投资有限责任公司",
             "国网湖南衡东县供电有限责任公司",
             "英大长安保险经纪有限公司",
             "国网湖南会同县供电有限责任公司",
             "湖南平江电力有限责任公司",
             "国网湖南节能服务有限公司",
             "湖南西洞庭电力有限责任公司",
             "英大长安保险经纪集团有限公司",
             "湖南屈原电力有限责任公司",
             "国网湖南中方县供电有限责任公司",
             "湖南电力交易中心有限公司",
             "大唐华银电力股份有限公司",
             "国网（湖南）电动汽车服务有限公司",
             "湖南黑麋峰抽水蓄能有限公司",
             "湖南电力实业开发总公司",
             "湖南省电网工程公司",
             "湖南交水建保险经纪有限公司",
             "湖南卓信高新财富基金管理有限公司",
             "湖南交通科学研究院有限公司",
             "湖南省疏浚有限公司",
             "湖南交通国际经济工程合作有限公司",
             "湖南省航务工程有限公司",
             "湖南省水利电力工程建设监理咨询有限公司",
             "湖南尚上建设开发有限公司",
             "湖南省交通规划勘察设计院有限公司",
             "长沙农村商业银行股份有限公司",
             "湖南国开铁路投资有限公司",
             "湖南国开铁路建设私募基金合伙企业（有限合伙）",
             "湖南国开铁路建设私募基金管理有限公司",
             "湖南铁路建设投资有限公司",
             "湖南省瓦松铁路建设投资有限责任公司",
             "湖南基础建设实业发展有限公司",
             "吉祥人寿保险股份有限公司",
             "方正证券股份有限公司",
             "长沙铁路福联实业有限公司",
             "国开发展湖南两型基金企业（有限合伙）",
             "长沙市城中村改造有限公司",
             "湖南有色金属有限公司",
             "湖南有色金属控股集团有限公司",
             "湖南省送变电工程公司",
             "湖南路桥建设集团有限责任公司",
             "湖南省公路建设投资有限公司",
             "国开发展湖南“两型”元盛基金企业（有限合伙）",
             "国开发展湖南“两型”基金企业（有限合伙）",
             "湖南湘江新区先导滨江私募基金发展合伙企业（有限合伙）"]
