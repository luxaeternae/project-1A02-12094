ó
a¤Yc           @   sŞ   d  d l  Z  e  j d d  Z e j   e j d d  d   Z d GHe d  Z e d	  Z e d
  Z	 e j
 d e e e  f d e e e  f d e	  d GHd S(   i˙˙˙˙Ns   smtp.gmail.comiK  s   happy0193472@gmail.coms   21122112Aa!c         C   sH   |  d k r d S|  d k r  d S|  d k r0 d S|  d k r@ d Sd	 Sd  S(
   Nt   Verizons	   vtext.comt   Sprints   messaging.sprintpcs.coms   AT&Ts   txt.att.nets   T-mobiles   tmomail.netsF   Provider invalid or unsupported. Contact app developer for assistance.(    (   t	   raw_input(    (    s
   sendsms.pyt   company   s    s   Welcome to HappyText v 1.1s   Phone Number/Contact:s	   Provider:s   Message:s   %s@%ss   %ss   Your message was sent!(   t   smtplibt   SMTPt   servert   starttlst   loginR   R   t   numbert   providet   textt   sendmail(    (    (    s
   sendsms.pyt   <module>   s   
	7