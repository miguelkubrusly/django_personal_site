from django.utils.text import slugify

def slugify_title(title):
  title_words = title.strip().split(" ")
  if len(title_words) > 5:
    title_words = title_words[:6]    
  formatted_title_words = [word.lower() for word in title_words]
  slug = slugify("-".join(formatted_title_words))
  return slug

posts_no_url = [
  {
    "id":0,
    "title":"Cillum irure mollit reprehenderit aliqua voluptate veniam eu",
    "content":"Sint aliquip velit tempor ut qui minim ipsum exercitation est esse incididunt elit est consequat. Non ea ipsum irure commodo consequat mollit. Exercitation tempor elit reprehenderit et excepteur. Nisi dolor dolore nostrud sunt Lorem mollit amet qui laborum minim et.\nIrure deserunt aliquip laborum aute occaecat Lorem elit dolor in ad incididunt. Irure tempor laborum mollit enim dolore ullamco fugiat elit. Adipisicing velit enim dolore fugiat enim anim quis sit velit nulla dolor. Voluptate nostrud dolor eiusmod voluptate sit aliquip sunt. Irure sit quis aliqua ex voluptate labore sit minim reprehenderit aliqua aute."
  },
  {
    "id":1,
    "title":"Elit officia commodo aute fugiat dolor ea",
    "content":"Sit aute cillum reprehenderit commodo irure duis minim mollit deserunt. Qui ad Lorem est id exercitation incididunt ea. Elit deserunt dolor Lorem nisi do veniam non. Exercitation deserunt reprehenderit esse labore anim sit incididunt enim in adipisicing.\nIrure eiusmod cillum velit Lorem do laboris mollit et. Tempor id et voluptate laborum laboris amet consectetur. Lorem esse non aliquip elit dolor nisi anim laboris cupidatat nulla ea et dolore aliqua. Pariatur aute adipisicing aliquip amet tempor irure cillum amet nisi sint exercitation minim esse laborum. Mollit esse eu ipsum minim. Irure ut mollit nostrud ex excepteur sint nostrud officia ex minim consectetur. Deserunt ullamco laboris reprehenderit ad."
  },
 {
    "id":2,
    "title":"Cillum irure mollit reprehenderit aliqua voluptate veniam eu",
    "content":"Sint aliquip velit tempor ut qui minim ipsum exercitation est esse incididunt elit est consequat. Non ea ipsum irure commodo consequat mollit. Exercitation tempor elit reprehenderit et excepteur. Nisi dolor dolore nostrud sunt Lorem mollit amet qui laborum minim et.\nIrure deserunt aliquip laborum aute occaecat Lorem elit dolor in ad incididunt. Irure tempor laborum mollit enim dolore ullamco fugiat elit. Adipisicing velit enim dolore fugiat enim anim quis sit velit nulla dolor. Voluptate nostrud dolor eiusmod voluptate sit aliquip sunt. Irure sit quis aliqua ex voluptate labore sit minim reprehenderit aliqua aute."
  },
  {
    "id":3,
    "title":"Elit officia commodo aute fugiat dolor ea",
    "content":"Sit aute cillum reprehenderit commodo irure duis minim mollit deserunt. Qui ad Lorem est id exercitation incididunt ea. Elit deserunt dolor Lorem nisi do veniam non. Exercitation deserunt reprehenderit esse labore anim sit incididunt enim in adipisicing.\nIrure eiusmod cillum velit Lorem do laboris mollit et. Tempor id et voluptate laborum laboris amet consectetur. Lorem esse non aliquip elit dolor nisi anim laboris cupidatat nulla ea et dolore aliqua. Pariatur aute adipisicing aliquip amet tempor irure cillum amet nisi sint exercitation minim esse laborum. Mollit esse eu ipsum minim. Irure ut mollit nostrud ex excepteur sint nostrud officia ex minim consectetur. Deserunt ullamco laboris reprehenderit ad."
  },{
    "id":4,
    "title":"Cillum irure mollit reprehenderit aliqua voluptate veniam eu",
    "content":"Sint aliquip velit tempor ut qui minim ipsum exercitation est esse incididunt elit est consequat. Non ea ipsum irure commodo consequat mollit. Exercitation tempor elit reprehenderit et excepteur. Nisi dolor dolore nostrud sunt Lorem mollit amet qui laborum minim et.\nIrure deserunt aliquip laborum aute occaecat Lorem elit dolor in ad incididunt. Irure tempor laborum mollit enim dolore ullamco fugiat elit. Adipisicing velit enim dolore fugiat enim anim quis sit velit nulla dolor. Voluptate nostrud dolor eiusmod voluptate sit aliquip sunt. Irure sit quis aliqua ex voluptate labore sit minim reprehenderit aliqua aute."
  },
  {
    "id":5,
    "title":"Elit officia commodo aute fugiat dolor ea",
    "content":"Sit aute cillum reprehenderit commodo irure duis minim mollit deserunt. Qui ad Lorem est id exercitation incididunt ea. Elit deserunt dolor Lorem nisi do veniam non. Exercitation deserunt reprehenderit esse labore anim sit incididunt enim in adipisicing.\nIrure eiusmod cillum velit Lorem do laboris mollit et. Tempor id et voluptate laborum laboris amet consectetur. Lorem esse non aliquip elit dolor nisi anim laboris cupidatat nulla ea et dolore aliqua. Pariatur aute adipisicing aliquip amet tempor irure cillum amet nisi sint exercitation minim esse laborum. Mollit esse eu ipsum minim. Irure ut mollit nostrud ex excepteur sint nostrud officia ex minim consectetur. Deserunt ullamco laboris reprehenderit ad."
  },
]

urls = [slugify_title(post["title"]) for post in posts_no_url]

posts = [{
  **post,
  "slug": slugify_title(post["title"]) 
} for post in posts_no_url]