function Str (str)
    return (str.text
    :gsub('%[%[', '')
    :gsub('%]%]', ''))
 end
