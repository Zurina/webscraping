import bs4
import requests
import matplotlib.pyplot as plt
import networkx as nx

start_url = 'http://www.kultunaut.dk/perl/arrlist/type-nynaut/UK?showmap=&Area=Kbh.+og+Frederiksberg&periode=&Genre=Musik'
start_url2 = 'http://www.pyregex.com/'

links_dic = {}
def find_all_links(url, depth): 
        try: 
            print(depth)
            if depth > 0:
                # Webscraping current url
                data = requests.get(url)
                soup = bs4.BeautifulSoup(data.text, 'html5lib')

                # finding current url's links and adding it to the dictionary as key = url, value = [links]
                links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
                links_dic[url] = links

                if len(links) != 0 and depth-1 > 0:
                    for link in links_dic.get(url): # runs through the current url's links
                        if not links_dic.get(link): # if the link already is a key in the dictionary
                            find_all_links(link, depth-1) # if no, webscrape that shit
                        else:
                            print('Link already found!') # if yes, continue to next one
        except:
            print('An error has happened..!')
        

def plot_links():
    find_all_links(start_url2, 2)
    print(len(links_dic.keys()))

    plot = []
    for key, links in links_dic.items():
        for link in links:
            plot.append((key, link, 1))

        
    DG = nx.DiGraph()
    DG.add_weighted_edges_from(plot)
    nx.draw_networkx(DG, node_color = "Green", node_size = 0.5, arrows = False, with_labels=False)
    plt.show()

plot_links()

