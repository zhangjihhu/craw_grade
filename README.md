# craw_grade
craw school grade

1、登录(post)

Request URL: http://202.119.112.195/hhu/login.action
    formdata{
        username
        passwpord
        x
        y
    }

2、培养管理(get)

Request URL: http://202.119.112.195/hhu/jsp/home/getChildMenu.action?menuid=3
  
  headers{
  
        Referer: http://202.119.112.195/hhu/login.action
        
    }

3、成绩查询

(get)Request URL: http://202.119.112.195/hhu/jsp/train/initSorceDetail.action?actType=1
	
  headers{
  
		Referer: http://202.119.112.195/hhu/jsp/home/getChildMenu.action?menuid=3
    
	}
  
(post)Request URL: http://202.119.112.195/hhu/jsp/train/getSorceDetail.action
	
  headers{
  
	    Referer: http://202.119.112.195/hhu/jsp/train/initSorceDetail.action?actType=1
      
	}
