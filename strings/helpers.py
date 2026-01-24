HELP_1 = """<b><u>ᴀᴅᴍɪɴ əᴍʀʟəʀɪ :</b></u>

Kanalda istifadə etmək üçün əmrlərin əvvəlinə <b>c</b> hərfi əlavə edin.

/pause : Hazırda ifa olunan yayımı dayandırır.
/resume : Dayandırılmış yayımı davam etdirir.
/skip : Hazırkı yayımı keçir və növbədəki mahnını başladır.
/end və ya /stop : Növbəni təmizləyir və yayımı bitirir.
/player : İnteraktiv pleyer panelini göstərir.
/queue : Növbədə olan mahnıların siyahısını göstərir.
"""

HELP_2 = """
<b><u>səʟᴀʜɪʏʏəᴛʟɪ (ᴀᴜᴛʜ) ɪsᴛɪғᴀᴅəçɪʟəʀ :</b></u>

Səlahiyyətli istifadəçilər qrupda admin olmasalar belə, botun admin hüquqlarından istifadə edə bilərlər.

/auth [istifadəçi adı/ID] : İstifadəçini botun səlahiyyətli siyahısına əlavə edir.
/unauth [istifadəçi adı/ID] : İstifadəçini səlahiyyətli siyahısından çıxarır.
/authusers : Qrupun səlahiyyətli istifadəçilərinin siyahısını göstərir.
"""

HELP_3 = """
<u><b>ʏᴀʏıᴍ (ʙʀᴏᴀᴅᴄᴀsᴛ) ᴋᴇʏғɪʏʏəᴛɪ</b></u> [Yalnız Sudolar üçün] :

/broadcast [mesaj və ya mesaja reply] : Botun xidmət etdiyi bütün qruplara mesaj göndərir.

<u>Yayım rejimləri:</u>
<b>-pin</b> : Göndərilən mesajı qruplarda bərkidir (pin).
<b>-pinloud</b> : Mesajı bərkidir və bütün üzvlərə bildiriş göndərir.
<b>-user</b> : Mesajı botu start edən bütün istifadəçilərə göndərir.
<b>-assistant</b> : Mesajı botun asistan hesabından göndərir.
<b>-nobot</b> : Mesajın bot tərəfindən göndərilməsini dayandırır.

<b>Nümunə:</b> <code>/broadcast -user -assistant -pin sınaq yayımı</code>
"""

HELP_4 = """<u><b>ǫʀᴜᴘ ǫᴀʀᴀ sɪʏᴀʜısı :</b></u> [Yalnız Sudolar üçün]

Botun istifadəsini istənilməyən qruplar üçün məhdudlaşdırın.

/blacklistchat [Qrup ID] : Qrupun botdan istifadəsini qadağan edir.
/whitelistchat [Qrup ID] : Qadağan olunmuş qrupu ağ siyahıya əlavə edir.
/blacklistedchat : Qara siyahıda olan qrupların siyahısını göstərir.
"""

HELP_5 = """
<u><b>ɪsᴛɪғᴀᴅəçɪ ʙʟᴏᴋʟᴀᴍᴀ:</b></u> [Yalnız Sudolar üçün]

İstifadəçini qara siyahıya salır ki, bot əmrlərindən istifadə edə bilməsin.

/block [istifadəçi adı və ya reply] : İstifadəçini botdan bloklayır.
/unblock [istifadəçi adı və ya reply] : İstifadəçinin blokunu açır.
/blockedusers : Bloklanmış istifadəçilərin siyahısını göstərir.
"""

HELP_6 = """
<u><b>ᴋᴀɴᴀʟ İғᴀ əᴍʀʟəʀɪ:</b></u>

Kanalda audio/video yayım edə bilərsiniz.

/cplay : Kanaldakı video söhbətdə audio yayımı başladır.
/cvplay : Kanaldakı video söhbətdə video yayımı başladır.
/cplayforce və ya /cvplayforce : Hazırkı yayımı dayandırır və seçilmiş mahnını dərhal başladır.

/channelplay [Qrup adı və ya ID] və ya [disable] : Kanalı qrupa bağlayır və qrupdan göndərilən əmrlərlə kanalda yayım edir.
"""

HELP_7 = """
<u><b>ǫʟᴏʙᴀʟ ʙᴀɴ (ɢʙᴀɴ)</b></u> [Yalnız Sudolar üçün] :

/gban [istifadəçi adı və ya reply] : İstifadəçini botun olduğu bütün qruplardan qlobal olaraq ban edir.
/ungban [istifadəçi adı və ya reply] : Qlobal banı ləğv edir.
/gbannedusers : Qlobal ban almış istifadəçilərin siyahısını göstərir.
"""

HELP_8 = """
<b><u>ᴛəᴋʀᴀʀ İғᴀ (ʟᴏᴏᴘ) :</b></u>

<b>Hazırkı yayımı döngüye salır.</b>

/loop [enable/disable] : Təkrar ifanı aktivləşdirir və ya söndürür.
/loop [1, 2, 3, ...] : Yayımı verilən say qədər təkrar edir.
"""

HELP_9 = """
<u><b>ᴛᴇxɴɪᴋɪ xɪᴅᴍəᴛ ʀᴇᴊɪᴍɪ</b></u> [Yalnız Sudolar üçün] :

/logs : Botun loqlarını (əməliyyat qeydlərini) əldə edir.

/logger [enable/disable] : Botda baş verən fəaliyyətlərin qeyd olunmasını başladır.

/maintenance [enable/disable] : Botun texniki xidmət rejimini aktivləşdirir və ya söndürür.
"""

HELP_10 = """
<b><u>ᴘɪɴɢ & sᴛᴀᴛɪsᴛɪᴋᴀ :</b></u>

/start : Musiqi botunu başladır.
/help : Əmrlərin izahı ilə kömək menyusunu göstərir.

/ping : Botun gecikmə sürətini və sistem statistikasını göstərir.

/stats : Botun ümumi statistikasını göstərir.
"""

HELP_11 = """
<u><b>İғᴀ əᴍʀʟəʀɪ :</b></u>

<b>v :</b> Video ifa deməkdir.
<b>force :</b> Məcburi (dərhal) ifa deməkdir.

/play və ya /vplay : Video söhbətdə istənilən mahnını/videonu başladır.

/playforce və ya /vplayforce : Hazırkı yayımı dayandırır və istənilən mahnını dərhal başladır.
"""

HELP_12 = """
<b><u>ɴöᴠʙəɴɪ ǫᴀʀışᴅıʀ (sʜᴜғғʟᴇ) :</b></u>

/shuffle : Növbədə olan mahnıları qarışdırır.
/queue : Qarışdırılmış növbəni göstərir.
"""

HELP_13 = """
<b><u>İʀəʟɪ/ɢᴇʀɪ çəᴋ (sᴇᴇᴋ) :</b></u>

/seek [saniyə] : Yayımı verilən saniyə qədər irəli çəkir.
/seekback [saniyə] : Yayımı verilən saniyə qədər geri çəkir.
"""

HELP_14 = """
<b><u>ᴍᴀʜɴı ʏüᴋʟə :</b></u>

/song [mahnı adı/YT linki] : YouTube-dan hər hansı bir mahnını MP3 və ya MP4 formatında yükləyir.
"""

HELP_15 = """
<b><u>sürəᴛ əᴍʀʟəʀɪ :</b></u>

Yayımın sürətinə nəzarət edə bilərsiniz. [Yalnız Adminlər]

/speed və ya /playback : Qrupda audio ifa sürətini tənzimləmək üçün.
/cspeed və ya /cplayback : Kanalda audio ifa sürətini tənzimləmək üçün.
"""

HELP_16 = """
<b><u>Məxfilik Əmri :</b></u>

/privacy : {0} botunun məxfilik bəyanatını göstərir.
"""
