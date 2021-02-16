o_url = self.videolink_lineEdit.text()
            yt = YouTube(video_url)
            self.title_label.setText("[Title] " + yt.title)    
            self.author_label.setText("[Author] " + yt.author)
            self.views_label.setText("[Views] " + str(yt.views))
            self.rating_label.setText("[Rating] " + str(yt.rating))
            self.time_label.setText("[Time(second)] " + str(yt.length))
            self.age_restricted_label.setText("[Age Restricted] " + str(yt.age_restricted))
            self.description_textEdit.setText(yt.description)
            print("[썸네일URL]", yt.thumbnail_url) # 썸네일 url 주소
            self.vlist = yt.streams.all()
            for i in range(len(self.vlist)):
                video_type = self.vlist[i].split(" ")
                if video_type[-1] == "type=\"video\"":
                    print("type=\"video\"")
                elif video_type[-1] == "type=\"audio\"":
                    