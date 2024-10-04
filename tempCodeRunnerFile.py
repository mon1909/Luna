        page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")

            team1_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")
            team2_elements = soup.find_all(class_="cb-ovr-flo")

            if team1_elements and team2_elements:
                team1 = team1_elements[0].get_text()
                team2 = team1_elements[1].get_text()
                team1_score = team2_elements[8].get_text()
                team2_score = team2_elements[10].get_text()

                print(f"{team1} : {team1_score}")
                print(f"{team2} : {team2_score}")

                notification.notify(
                    title="IPL SCORE",
                    message=f"{team1} : {team1_score}\n{team2} : {team2_score}",
                    timeout=15
                )
            else:
                print("Unable to find elements on the webpage")