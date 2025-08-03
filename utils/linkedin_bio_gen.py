def generate_linkedin_bio(user_name, skills, experience, achievements):
    bio_template = (
        f"Hi, I'm {user_name}, a professional with expertise in {', '.join(skills)}. "
        f"I have {experience} years of experience in the industry, where I have successfully "
        f"achieved {achievements}. I am passionate about leveraging my skills to contribute "
        f"to innovative projects and collaborate with like-minded professionals."
    )
    return bio_template

def create_bio(user_info):
    user_name = user_info.get('name', 'User')
    skills = user_info.get('skills', [])
    experience = user_info.get('experience', 'N/A')
    achievements = user_info.get('achievements', 'notable accomplishments')
    
    return generate_linkedin_bio(user_name, skills, experience, achievements)