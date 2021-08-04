from appium import webdriver
import time
dc={
    "platformName": "android",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appWaitDuration": "5000",
    "appExecTimeout": "50000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "appPackage": "com.ATG.World",
    "deviceName": "emulator-5554",
    "driver": "http://localhost:4723/wd/hub"
}
# initializing webdriver with desired capabilities
driver=webdriver.Remote('http://localhost:4723/wd/hub',dc)

# allow for storage
chb=driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
chb.click()
time.sleep(2)

# starting to enter app
getStarted=driver.find_element_by_id("com.ATG.World:id/getStartedTv")
getStarted.click()
time.sleep(2)
sign=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]")
sign.click()
time.sleep(2)

# sign in 
username=driver.find_element_by_id("com.ATG.World:id/email")
time.sleep(1)
username.send_keys("wiz_saurabh@rediffmail.com")
passw=driver.find_element_by_id("com.ATG.World:id/password")
time.sleep(1)
passw.send_keys("Pass@123")
butt=driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
butt.click()
time.sleep(3)

# clicking got it buttons 2 times
gi=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
gi.click()
time.sleep(3)
gi=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView[2]")
gi.click()

# waiting for home to load
time.sleep(5)

# clicking button to get options
pencilFab=driver.find_element_by_id("com.ATG.World:id/fab")
pencilFab.click()
time.sleep(3)

# clicking on post image button
imagefab=driver.find_element_by_id("com.ATG.World:id/image_fab_clicked")
imagefab.click()
time.sleep(3)

# choosing post by camera and not by gallery
per=driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
per.click()
time.sleep(2)
# allowing camera permission
per_cam=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
per_cam.click()
time.sleep(3)
# clicking photo
click_but=driver.find_element_by_id("com.android.camera2:id/shutter_button")
click_but.click()
time.sleep(3)
# clicking done 
done_but=driver.find_element_by_id("com.android.camera2:id/done_button")
done_but.click()
time.sleep(3)

# adding caption to post
caption=driver.find_element_by_id("com.ATG.World:id/postCaption")
time.sleep(1)
caption.send_keys("Posted by tester bot !")
time.sleep(1)
# selecting group 1 and 3
slgroup=driver.find_element_by_id("com.ATG.World:id/layout_select_group_container")
slgroup.click()
time.sleep(2)
grp=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.TextView")
grp.click()
time.sleep(1)
grp=driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView")
grp.click()
time.sleep(1)

# closing group lauyout
x=driver.find_element_by_id("com.ATG.World:id/layout_group_list_close")
x.click()
time.sleep(3)
# clicking to post 
post_post=driver.find_element_by_id("com.ATG.World:id/toolbar_post_action")
post_post.click()
time.sleep(3) 

# going back from aour post to home
post_det_back=driver.find_element_by_id("com.ATG.World:id/post_details_back")
post_det_back.click()
time.sleep(3)
cross=driver.find_element_by_id("com.ATG.World:id/cross_fab_clicked")
cross.click()
time.sleep(3)
home=driver.find_element_by_id("com.ATG.World:id/nav_home")
home.click()
time.sleep(100)

