from email.message import EmailMessage
import ssl
import smtplib

# Create email variables
email_sender = 'shwelegugu@gmail.com'
email_password = 'ngrtiswlqhxajwdg'
email_receiver = 'hakkirurto@gufum.com'

# Content of email
subject = "Don't Miss Out on Our Epic Sale! 🎉"
body = """
Dear valued customer,

We are thrilled to announce an incredible sale event happening at Stylista Boutique. Get ready for jaw-dropping discounts and unbeatable deals that you won't want to miss!

<b>🌟 Huge Savings Await You:</b><br>
From fashionable apparel to trendy accessories, home decor to tech gadgets, our store is brimming with amazing products, and now is the perfect time to shop. Take advantage of our exclusive sale to upgrade your wardrobe, enhance your living space, or find that perfect gift for your loved ones.

<b>🛍️ Unbeatable Discounts:</b><br>
We've slashed prices storewide, offering discounts of up to 50 percent off on selected items. Whether you've had your eye on that stylish dress, the latest electronic gadget, or something special for your home, now is the time to indulge in your shopping desires without breaking the bank.

<b>📅 Mark Your Calendar:</b><br>
The sale starts on 24 August and will continue until 15 September. Remember, the early bird catches the best deals, so make sure to visit our store as soon as the doors open. Our friendly and knowledgeable staff will be ready to assist you in finding the perfect items and ensuring your shopping experience is delightful.

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)



em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
