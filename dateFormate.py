

import re

def custom_date_format(date_string):
   dd_mm_yyyy=r'(\d{2})-(\d{2})-(\d{4})' 
   yyyy_mm_dd=r'(\d{4})-(\d{2})-(\d{2})' 
   mm_dd_yyyy=r'(\d{2})-(\d{2})-(\d{4})' 
    
   if re.match( yyyy_mm_dd,date_string):
      return re.sub( yyyy_mm_dd,r'\3-\2-\1',date_string)
   
   elif re.match(mm_dd_yyyy,date_string):
       return re.sub( mm_dd_yyyy,r'\2-\1-\3',date_string)
   
   else:
      return "Ivalid date format"