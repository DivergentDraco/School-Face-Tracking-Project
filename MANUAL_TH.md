# คู่มือการใช้งานโปรแกรมติดตามใบหน้า (Face Tracking Manual)

## 2302307 Interactive Science and Social Project (ISSP) ปีการศึกษา 2024

[อ่านคู่มือโปรแกรมติดตามดวงตาได้ที่นี่](https://github.com/DivergentDraco/School-Eye-Gaze-Project/blob/main/MANUAL_TH.md)

[อ่านคู่มือฉบับภาษาอังกฤษได้ที่นี่ | Click here for English version](README.md)

---

# บทนำ

โปรแกรมติดตามใบหน้าเป็นอีกทางเลือกหนึ่งเพื่อตอบสนองต่อปัญหาที่เกิดขึ้นจากการใช้โปรแกรมติดตามดวงตา โครงงานนี้ถูกทำขึ้นมาหลังจากการวิเคราะห์ปัญหาที่พบจากโรงเรียนศรีสังวาลย์ผ่านการถามคำถาม การสัมภาษณ์ปากเปล่า และการตอบแบบสำรวจกับคุณครู ผู้อำนวยการ ศิษย์เก่า และผู้ที่ทำงานในโรงเรียนศรีสังวาลย์

พื้นที่เก็บข้อมูลนี้ถูกจัดทำขึ้นภายใต้โครงงานในวิชา Interactive Science and Social Project ซึ่งเป็นหนึ่งในวิชาของนิสิตสาขาเคมีประยุกต์นานาชาติ ภาควิชาเคมีคณะวิทยาศาสตร์จุฬาลงกรณ์มหาวิทยาลัย ร่วมมือกับทาง Worscester Polytechnic Institute จากประเทศสหรัฐอเมริกา โดยมีโรงเรียนศรีสังวาลย์เป็นผู้สนับสนุน หนึ่งในประเด็นที่ผู้จัดทำสนใจอีกอย่างหนึ่งคือการใช้โปรแกรมภายนอกที่สามารถติดตามการเคลื่อนไหวของดวงตาด้วยการเคลื่อนไหวของใบหน้า

---

## สมาชิก
 * Sean Arackal, *Worcester Polytechnic Institute*
 * Mohamed Adem Djadid, *Worcester Polytechnic Institute*
 * ภวินท์ หริจันทร์วงศ์, *จุฬาลงกรณ์มหาลัย* ([@DivergentDraco](https://github.com/DivergentDraco))
 * สิรภพ หอมหวล, *จุฬาลงกรณ์มหาลัย*
 * Madalyn Nguyen, *Worcester Polytechnic Institute*
 * มาริสา รุกขจันทรกุล, *จุฬาลงกรณ์มหาลัย*
 * ภูริณัฐ สุเมธโชติเมธา, *จุฬาลงกรณ์มหาลัย*
 * Mahit Verma, *Worcester Polytechnic Institute* ([@MaVeryo](https://github.com/MaVeryo))

---

# ภาพรวมของโครงงาน

**โรงเรียนศรีสังวาลย์ จังหวัดนนทบุรี** เป็นโรงเรียนที่มีระบบการศึกษาแบบกลุ่มเพื่อการเรียนรู้สำหรับผู้ที่มีความพิการ ซึ่งเป้าหมายโครงงานนี้คือการเขียนคำแนะนำเพื่อพัฒนาและแก้ไขปัญหาที่มีอยู่ในโรงเรียนและทำให้การศึกษาเชิงดิจิทัลของโรงเรียนดีมากขึ้น

โครงงานนี้เน้นให้การชี้แนะแนวทางพัฒนาผ่านการทำแบบสอบถาม การสัมภาษณ์ และการสังเกตการณ์ในห้องเรียน แต่หลังจากที่ผู้จัดทำได้ทดลองใช้โปรแกรมติดตามดวงตา จึงได้ข้อสรุปว่าโปรแกรมติดตามใบหน้าเป็นอีกทางเลือกหนึ่งที่อาจมีความเสถียรมากกว่า ไม่มีการปวดตา และมีความแม่นยำกว่าการจับดวงตา 

จุดที่แตกต่างระหว่างสองโปรแกรมนี้นั่นคือ\
สำหรับโปรแกรมติดตามดวงตา กล้องจะติดตามที่ดวงตาเท่านั้น หากหลับตาหรือขยับศีรษะไปที่อื่นจะทำให้ต้องตั้งค่า (calibrate) ใหม่\
ในขณะที่โปรแกรมติดตามใบหน้า กล้องจะติดตามดวงตาเช่นกัน แต่หากใบหน้าขยับเคอร์เซอร์เมาส์บนจอ ก็จะขยับตามไปด้วย ทำให้มีความแม่นยำที่สูงกว่า

![School Banner](https://github.com/user-attachments/assets/9b123cf6-f919-4abe-b54b-365a5b79b447)

## เป้าหมาย
เป้าหมายของโครงงานนั้นคือ“การพัฒนาเทคโนโลยีสิ่งอำนวยความสะดวกเพื่อทักษะด้านคอมพิวเตอร์ของโรงเรียนศรีสังวาลย์” ซึ่งมีนักเรียนที่อวัยวะขาดหาย ภาวะสมองพิการ หรือภาวะอื่นๆที่เกี่ยวข้อง

### ภาษาโค้ดดิ้งที่ใช้
#### ในการที่จะใช้โค้ดในไฟล์นี้ ท่านต้องมีโปรแกรมดังกล่าว:
##### โปรแกรมที่จำเป็น
  - Python **3.9.13** ([Website](https://www.python.org/downloads/release/python-3913/))
  - ไฟล์ในพื้นที่เก็บข้อมูลนี้

##### อุปกรณ์ที่จำเป็น
  - **กล้อง Webcam** เป็นอุปกรณ์ที่จำเป็นในการจับใบหน้าซึ่งไม่จำเป็นที่จะต้องใช้กล้องที่ภาพละเอียดมาก แต่การจับวีดีโอควรมีอัตราเฟรม (framerate) ที่เร็วพอ
ซึ่งแนะนำว่าใช้กล้อง Logitech C270 HD จะมีความคุ้มค่ามากที่สดเนื่องจากมีราคาประมาณ 590 บาท

# วีดีโอสาธิตการใช้งาน
[กดลิ้งก์ที่นี่]()

---

# การติดตั้ง

## วีดีโอสาธิตการติดตั้ง
[กดลิ้งก์ที่นี่]()

## ขั้นตอนการติดตั้ง
1. ติดตั้งโปรแกรมเหล่านี้\
 1.1 Python 3.9.13\
 1.2 Code Editor (เช่น Visual Studio Code)\
2. ติดตั้งไฟล์ในrepositoryนี้\
 2.1 เปิดโฟลเดอร์ไฟล์ จากนั้นให้กดไปที่โฟลเดอร์ *API* และกดไปที่โฟลเดอร์ *Python*\
 2.2 เปิดไฟล์ **tracker_sample.py**


หากท่านสามารถรันโค้ดได้อย่างถูกต้อง กล้องwebcamจะเปิดขึ้น ซึ่งควรมีผลลัพธ์เหมือนภาพนี้\
![image](https://github.com/user-attachments/assets/433db1c6-cb31-4e86-a944-ff082d356696)

---

> [!คำเตือน]
> วิธีนี้ไม่จำเป็นต้องเสียค่าใช้จ่ายกับโปรแกรม

> [!คำเตือน]
> โครงงานทดลองโปรแกรมติดตามใบหน้านี้อยู่ในระหว่างการปรับปรุงการใช้งานซึ่งไม่ได้เจตนาที่จะนำมาใช้งานจริงด้วยหลายปัญหา อย่างเช่นการปรับหน้าและตา รวมทั้งปัญหาความอ่อนไหวของโปรแกรมติดตามดวงตาผ่านใบหน้า โครงงานทดลองนี้ทำขึ้นเพื่อนำมาประกอบการตัดสินใจกับทางโรงเรียนและเพื่อให้ทีมผู้พัฒนาที่ต้องการทำต่อมาประกอบกับการตัดสินใจ

โดยสรุป โปรแกรมติดตามใบหน้านี้มีข้อบกพร่องน้อยกว่าโปรแกรมติดตามดวงตามาก ซึ่งมีโอกาสที่สามารถเอามาใช้งานได้ถ้าเขียนถูกวิธี

# ปัญหาที่พบเจอ
การขยับศีรษะและคอ
นักเรียนอาจปวดคอหรือการขยับคอผิดปกติ ซึ่งระหว่างการพัฒนาควรนำมาลองใช้ และเลือกนักเรียนที่ไม่มีปัญหาเหล่านี้

หากประสบปัญหาหรือเกิดปัญหาใดๆก็ตามกับโปรแกรม โปรดส่งข้อความมาที่อีเมล Srisangwanissp@gmail.com
