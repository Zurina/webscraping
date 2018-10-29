import bs4
import requests
import matplotlib.pyplot as plt
import networkx as nx

start_url = 'http://www.kultunaut.dk/perl/arrlist/type-nynaut/UK?showmap=&Area=Kbh.+og+Frederiksberg&periode=&Genre=Musik'
start_url2 = 'http://www.pyregex.com/'

all_links = []
count = 0

# # returns a list of all links
# def find_all_links_in_links(url, depth): # depth = 2 is preferred - otherwise way too long runtime
#     try: 
#         print(depth)
#         if depth > 0:
#             #print(len(all_links))
#             data = requests.get(url)
#             soup = bs4.BeautifulSoup(data.text, 'html5lib')
#             links = [a['href'] for a in soup.find_all('a', href=True) if a.text]
#             if len(links) != 0:
#                 for link in links:
#                     if(link.startswith('http') and link not in all_links):
#                         print(link)
#                         all_links.append(url)
#                         find_all_links_in_links(link, depth-1)
#                     else:
#                         print('Link already found!')
#     except:
#         print('An error has happened..!')

#find_all_links_in_links(start_url2, 3)
#print(len(all_links))

# dictionary example
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
                            find_all_links(link, depth-1) # if yes, webscrape that shit
                        else:
                            print('Link already found!') # if no, continue to next one
        except:
            print('An error has happened..!')
        

def plot_links():
    find_all_links(start_url2, 2)
    print(len(links_dic.keys()))

    # Use Helge reference for creating plt
    plot = []
    for key, links in links_dic.items():
        for link in links:
            plot.append((key, link, 1))

        
    DG = nx.DiGraph()
    DG.add_weighted_edges_from(plot)
    nx.draw_networkx(DG, node_color = "Green", node_size = 0.5, arrows = False, with_labels=False)
    plt.show()

plot_links()

