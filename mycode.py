from playwright.sync_api import Page, expect

def test_mycode(page:Page):
    page.goto("https://automationexercise.com/", wait_until='networkidle')
    heading=page.locator("img[alt='Website for automation practice']")
    expect(heading).to_be_visible(timeout=10000)

    login=page.get_by_role("link", name="Signup / Login")
    login.click()

    signup_visible=page.get_by_role("heading", name="New User Signup!")
    expect(signup_visible).to_be_visible(timeout=1000)

    page.get_by_role("textbox", name="Name").fill("Samrat Ghimire")
    page.locator("//input[@data-qa='signup-email']").fill("samratghimire7@gmail.com")
    page.get_by_role("button", name="Signup").click()

    vis2=page.locator("b:has-text('ENTER ACCOUNT INFORMATION')")
    expect(vis2).to_be_visible()

    page.pause()

    page.get_by_role("radio", name="Mr.").click()
    
    page.get_by_label("Password *").fill("12132")

    page.locator("#days").select_option("4")

    page.locator("#months").select_option("December")

    page.locator("#years").select_option("2000")

    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()

    page.get_by_role("checkbox", name="Receive special offers from our partners!").check()

    page.get_by_role("textbox", name="First name *").fill("Balkhu")

    page.get_by_role("textbox", name="Last name *").fill("Kathmandu")

    page.get_by_label("Company", exact=True).fill("Katmatic")

    page.get_by_role("textbox", name="Address * (Street address, P.O. Box, Company name, etc.)").fill("Balkhu")

    page.get_by_role("textbox", name="Address 2").fill("Kathmandu")

    page.get_by_role("combobox", name="Country *").select_option("Canada")

    page.get_by_role("textbox", name="State *").fill("290 Bremner Blvd")

    page.get_by_role("textbox", name="City *").fill("Toronto")

    page.locator("#zipcode").fill("•  M5V 3L9")

    page.get_by_role("textbox", name="Mobile Number *").fill("98888888")

    page.get_by_role("button", name="Create Account").click()

    vis3=page.locator("b:has-text('ACCOUNT CREATED!')")

    expect(vis3).to_be_visible()

    page.get_by_role("link", name="Continue").click()

    vis4=page.get_by_text("Logged in as samrat ghimire")

    expect(vis4).to_be_visible()

    page.pause()

    page.get_by_role("link", name="Delete Account").click()

    vis5=page.locator("b:has-text('ACCOUNT DELETED!')")

    expect(vis5).to_be_visible()

    page.get_by_role("link", name="Continue").click()

    page.wait_for_timeout(10000)

