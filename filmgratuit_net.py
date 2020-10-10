# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# source 04 # remise a jour 08102020

import re
import requests
import base64

from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
from resources.lib.util import Unquote

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'


SITE_IDENTIFIER = 'filmgratuit_net'
SITE_NAME = 'Filmgratuit'
SITE_DESC = 'Films,Séries'

URL_MAIN = 'https://wvw.filmgratuit.net/'
URL_SEARCH = (URL_MAIN + 'index.php?do=search&subaction=search&story=', 'showMovies')
URL_SEARCH_MOVIES = (URL_SEARCH[0], 'showMovies')
URL_SEARCH_SERIES = (URL_SEARCH[0], 'showMovies')
URL_SEARCH_ANIMS = (URL_SEARCH[0], 'showMovies')


MOVIE_MOVIE = (True, 'showMenuMovies')
MOVIE_NEWS = (URL_MAIN + 'films.html', 'showMovies')

# Ajout TAG pour differncier  requete
MOVIE_NOTES = (URL_MAIN+ '#Films Box Office', 'showMovies') 
MOVIE_VIEWS = (URL_MAIN+ '#Films populaires' , 'showMovies') 

MOVIE_GENRES = (True, 'showMovieGenre')
MOVIE_YEARS= (True, 'showMovieYears')
MOVIE_PAYS= (True, 'showMoviePays')

MOVIE_HDRIP = (URL_MAIN + 'films/qualite/hdrip.html', 'showMovies')
MOVIE_BDRIP = (URL_MAIN + 'films/qualite/bdrip.html', 'showMovies')
MOVIE_DVDRIP = (URL_MAIN + 'films/qualite/dvdrip.html', 'showMovies')
MOVIE_WEBRIP = (URL_MAIN + 'films/qualite/webrip.html', 'showMovies')
MOVIE_HDTV = (URL_MAIN + 'films/qualite/hdtv.html', 'showMovies')
MOVIE_HD720 = (URL_MAIN + 'films/qualite/hd720.html', 'showMovies')

MOVIE_Vf = (URL_MAIN + 'films/langue/vf.html', 'showMovies')
MOVIE_VOSTFR = (URL_MAIN + 'films/langue/vostfr.html', 'showMovies')  # films VOSTFR
MOVIE_VO = (URL_MAIN + 'films/langue/vo.html', 'showMovies')

SERIE_SERIES = (True, 'showMenuSeries')
SERIE_GENRES = (True, 'showSerieGenre')
SERIE_NEWS = (URL_MAIN + 'series.html', 'showMovies')
SERIE_YEARS= (True, 'showSerieYears')

SERIE_NEWS_SAISONS=(URL_MAIN+'#Dernières saisons' , 'showMovies')
SERIE_NEWS_EPISODES=(URL_MAIN+'#Derniers épisodes' , 'showMovies')

MOVIE_VIEWS = (URL_MAIN+'#Films Box Office' , 'showMovies') #films (les plus vus = populaire)
MOVIE_NOTES = (URL_MAIN+ '#LES PLUS POPULAIRES', 'showMovies')

def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showMenuMovies', 'Films', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showMenuSeries', 'Séries', 'series.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()


def showMenuMovies():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_SEARCH_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Rechercher films', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oOutputParameterHandler.addParameter('sTag', 'Derniers ajouts' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Derniers ajouts' ,'news.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NOTES[0])
    oOutputParameterHandler.addParameter('sTag', 'les mieux notés' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NOTES[1], 'les mieux notés', 'notes.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VIEWS[0])
    oOutputParameterHandler.addParameter('sTag', 'les plus vus' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VIEWS[1], 'les plus vus', 'views.png', oOutputParameterHandler)   

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oOutputParameterHandler.addParameter('sTag', 'Genres' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oOutputParameterHandler.addParameter('sTag', 'Années' )
    oGui.addDir(SITE_IDENTIFIER, 'showMovieYears', 'Films (Par années)', 'annees.png', oOutputParameterHandler)  
    #
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_Vf[0])
    oOutputParameterHandler.addParameter('sTag', 'Langue' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_Vf[1], 'Films (VF)', 'vf.png', oOutputParameterHandler)
      
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VOSTFR[0])
    oOutputParameterHandler.addParameter('sTag', 'Langue' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VOSTFR[1], 'Films (VOSTFR)', 'vostfr.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_Vf[0])
    oOutputParameterHandler.addParameter('sTag', 'Langue' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VO[1], 'Films (VO)', 'vf.png', oOutputParameterHandler)
    #
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HDTV[0])
    oOutputParameterHandler.addParameter('sTag', 'Qualité' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_HDTV[1], 'Films (HDTV)', 'hd.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HD720[0])
    oOutputParameterHandler.addParameter('sTag', 'Qualité' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_HD720[1], 'Films (HD720)', 'hd.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HDRIP [0])
    oOutputParameterHandler.addParameter('sTag', 'Qualité' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_HDRIP [1], 'Films (HDRIP )', 'hd.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_DVDRIP[0])
    oOutputParameterHandler.addParameter('sTag', 'Qualité' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_DVDRIP[1], 'Films (DVDRIP)', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_BDRIP[0])
    oOutputParameterHandler.addParameter('sTag', 'Qualité' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_BDRIP[1], 'Films (BDRIP)', 'films.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_WEBRIP[0])
    oOutputParameterHandler.addParameter('sTag', 'Qualité' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_WEBRIP[1], 'Films (WEBRIP)', 'films.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_PAYS[0])
    oOutputParameterHandler.addParameter('sTag', 'Pays' )
    oGui.addDir(SITE_IDENTIFIER, MOVIE_PAYS[1], 'Pays', 'vf.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()


def showMenuSeries():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', URL_SEARCH_SERIES[0])
    oOutputParameterHandler.addParameter('sTag', 'Rechercher séries' )
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Rechercher séries', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    #oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Derniers ajouts', 'news.png', oOutputParameterHandler)
    oOutputParameterHandler.addParameter('sTag', 'Séries' )
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries ', 'news.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS_SAISONS[0])
    oOutputParameterHandler.addParameter('sTag', 'Dernieres saisons' )
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS_SAISONS[1], 'Séries (Dernieres saisons)', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS_EPISODES[0])
    oOutputParameterHandler.addParameter('sTag', 'Derniers épisodes' )
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS_EPISODES[1], 'Séries (Derniers épisodes)', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    oOutputParameterHandler.addParameter('sTag', 'Genres' )
    oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_YEARS[0])
    oOutputParameterHandler.addParameter('sTag', 'Années' )
    oGui.addDir(SITE_IDENTIFIER, SERIE_YEARS[1], 'Séries (Par Années)', 'annees.png', oOutputParameterHandler) 
    
    oGui.setEndOfDirectory()
    
def showSearch():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
        sUrl = sUrl + sSearchText + '&search_start=1'
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showMovieGenre():
    oGui = cGui()
    listeGenres = ['action', 'animation', 'arts-martiaux', 'aventure', 'biopic', 
                   'comédie','comédie-dramatique','comédie-musicale',  'documentaire', 
                   'drame', 'epouvante-horreur', 'erotique', 'espionnage','famille', 
                   'fantastique', 'guerre', 'historique', 'musical', 'péplum',
                   'policier', 'romance', 'science-fiction', 'thriller', 'western']
    
    for genre in listeGenres:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN  +'films/'+ genre )
        oOutputParameterHandler.addParameter('sTag', genre.capitalize() )
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', genre.capitalize(), 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSerieGenre():
    oGui = cGui()
    listeGenres = ['action', 'animation', 'arts-martiaux', 'aventure', 'biopic', 
                   'comédie','comédie-dramatique','comédie-musicale',  'documentaire', 
                   'drame', 'epouvante-horreur', 'erotique', 'espionnage','famille', 
                   'fantastique', 'guerre', 'historique', 'musical', 'péplum',
                   'policier', 'romance', 'science-fiction', 'thriller', 'western']
  
    for genre in listeGenres:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN  +'series/'+ genre )
        oOutputParameterHandler.addParameter('sTag', genre.capitalize() )
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', genre.capitalize(), 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    
def showMoviePays():
    oGui = cGui()
    listePays = ['allemagne', 'australie', 'autriche', 'belgique', 'bresil', 
                   'canada','chine','colombie',  'cuba', 
                   'danemark', 'espagne', 'egypte', 'finlande','france', 'grande-Bretagne',
                    'grece','inde', 'indonesie', 'irlande', 'israel', 'italie', 'japon',
                   'liban', 'luxembourg', 'malaisie', 'maroc', 'mexique', 'nigeria', 'norvegien',
                    'palestine', 'pologne', 'portugal','roumanie', 'russie', 'ukraine', 'uruguay'
                   'roumanie', 'suisse', 'suede', 'usa']
      
    for pays in listePays :
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN  +'films/nationalite/'+ pays + '.html' )
        oOutputParameterHandler.addParameter('sTag', pays.capitalize() )
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', pays.capitalize(), 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    
def showSeriePays():
    oGui = cGui()
    listePays = ['allemagne', 'australie', 'autriche', 'belgique', 'bresil', 
                   'canada','chine','colombie',  'cuba', 
                   'danemark', 'espagne', 'egypte', 'finlande','france', 'grande-Bretagne',
                    'grece','inde', 'indonesie', 'irlande', 'israel', 'italie', 'japon',
                   'liban', 'luxembourg', 'malaisie', 'maroc', 'mexique', 'nigeria', 'norvegien',
                    'palestine', 'pologne', 'portugal','roumanie', 'russie', 'ukraine', 'uruguay'
                   'roumanie', 'suisse', 'suede', 'usa']
      
    for pays in listePays :
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN  +'series/'+ pays + '.html' )
        oOutputParameterHandler.addParameter('sTag', pays.capitalize() )
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', pays.capitalize(), 'genres.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()



def showMovieYears():
    oGui = cGui()
    for i in reversed (range(1980, 2021)): 
        Year = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'films/annee/' + Year+'.html')
        oOutputParameterHandler.addParameter('sTag', Year )
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', Year, 'annees.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()
    
def showSerieYears():
    oGui = cGui()  
    for i in reversed (range(1990, 2021)):  
        Year = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'series/annee/' + Year +'.html')
        oOutputParameterHandler.addParameter('sTag', Year )
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', Year, 'annees.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def showMovies(sSearch=''):
    
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sTag=oInputParameterHandler.getValue('sTag')
     
    if sSearch:
        sUrl = sSearch
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    sPattern = 'th-in" href="([^"]+).+?src="([^"]+)" alt="([^"]+).+?th-tip-meta.+?(?:|<span>([^\D]+).+?)#aaa;">([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    
    VSlog('#### BEGIN TESTE URL = '+ sUrl)
    TAGTest=''
    
    sPatternFilm='short-images.+?ref="([^"]*)".+?src=".([^"]*).+?alt="([^"]*).+?qualite.(.+?).html.+?langue.(.+?).html'
    #   URL_MAIN 
    if (sUrl == MOVIE_NOTES[0] ) :#10 les mieux notes Films Box Office 
        firstIndex = sHtmlContent.index('Films Box Office')
        lastIndex = sHtmlContent.index('LES PLUS POPULAIRES') 
        if firstIndex >0 and lastIndex > 0 :
            sHtmlContent= sHtmlContent[firstIndex:lastIndex ]
        #url image title quality lang
        sPattern = 'images">.+?ref="([^"]*)".+?title="([^"]*)".+?src=".([^"]*)".+?qualite.+?"([^<]*)<.+?lang.+?class="([^"]*)"'
        sPattern= sPatternFilm
        aResult = oParser.parse(sHtmlContent, sPattern)#
        TAGTESTE='(TAG sUrl == MOVIE_NOTES[0] )'
    
    elif (sUrl == MOVIE_VIEWS[0]) : # 
        firstIndex = sHtmlContent.index('LES PLUS POPULAIRES')
        lastIndex = sHtmlContent.index('Films Récemment Ajoutés') 
        if firstIndex >0 and lastIndex > 0 :
            sHtmlContent= sHtmlContent[firstIndex:lastIndex ]
            
        # url image name
        
        sPattern = 'images">.+?ref="([^"]*)".+?src=".([^"]*)".+?alt="([^"]*)"'
        aResult = oParser.parse(sHtmlContent, sPattern)#
        TAGTESTE='(TAG sUrl == MOVIE_VIEWS[0])'
    
    elif (sUrl == SERIE_NEWS_SAISONS[0]) : # Derniers épisodes Séries-TV ajoutée
        
        #href="([^"]*).>([^"]*)Saison([^<]*).+?.total_eps">([^<]*)
        #surl  title 
        sPattern = 'href="([^"]*).>([^"]*)<span class="total'
        
        aResult = oParser.parse(sHtmlContent, sPattern)
        TAGTESTE='(TAG sUrl == SERIE_NEWS_SAISONS[0])'
   
    elif (sUrl == SERIE_NEWS_EPISODES[0]) : #Derniers épisodes 
    
        #url title lang
        sPattern = '<li><a href="([^"]*)">([^<]*).+?class="langue.([^"]*)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        TAGTESTE='TAG  (sUrl == SERIE_NEWS_EPISODES[0])'
    
   
    #   URL_MAIN / serie or films
    elif ( '/films' in sUrl ) :
          
        #url image title quality lang

        sPattern = 'short-images.+?ref="([^"]*)".+?src=".([^"]*).+?alt="([^"]*).+?qualite.+?"([^<]*)<.+?langue.+?">([^<]*)'
        sPattern= sPatternFilm
        aResult = oParser.parse(sHtmlContent, sPattern)
    
        TAGTESTE= '(TAG FilmsS in sUrl)'
    
    elif ( '/series' in sUrl ) :  
        
        #url image title
        #VSlog(sHtmlContent )
        sPattern = 'images radius.+?ref=".([^"]*)".+?src=".([^"]*).+?alt="([^"]*)"'# spat01 "inutile
        aResult = oParser.parse(sHtmlContent, sPattern)
    
        TAGTESTE= '(TAG serie in sUrl)'
        if (aResult[0] == False):
        
            VSlog('##### /series aResult[0] = False' )
    
    else:
        
        TAGTESTE= '(TAG  NO FIND)'
        sPattern = 'images radius.+?ref="([^"]*)".+?src=".([^"]*).+?alt="([^"]*)' ## spat01
        #url     image   short title
        aResult = oParser.parse(sHtmlContent, sPattern)
        #oGui.setEndOfDirectory()
        #return
    
    VSlog('##### TAGTESTE = ' + TAGTESTE)
    
    if (aResult[0] == False):
        
        VSlog('##### aResult[0] = False' )
        oGui.addText(SITE_IDENTIFIER)
    
    if (aResult[0] == True):
        
        VSlog('##### aResult[0] = True' )
        total = len(aResult[1])
        #progress_ = progress().VScreate(SITE_NAME)
        sDesc = '#'
        if sTag!=False :
            sDesc=sTag
            sDesc='[COLOR skyblue]'+ sTag+ '[/COLOR]'
            VSlog('#### Find tag = '+ sTag)
        
        for aEntry in aResult[1]:
            
            sUrl2 = aEntry[0]
            if not URL_MAIN in aEntry[0]:
                sUrl2 = URL_MAIN +aEntry[0]
            
            sThumb = ''
            sYear = ''
            sLang = ''
            sQuality = ''
            
            #progress_.VSupdate(progress_, total)
            #if progress_.iscanceled():
                #break
            
            if (sUrl == MOVIE_NOTES[0] ) :#10 les mieux notes Films Box Office 
                # url image title quality lang
                sTitle = aEntry[2]
                sThumb = aEntry[1]
                sLang = aEntry[4]
                sQuality = aEntry[3]
           
            elif (sUrl == MOVIE_VIEWS[0]) : # 
                # url image title
                sTitle = aEntry[2]
                sThumb = aEntry[1] 
                sDesc= 'Films Populaires '
            elif (sUrl == SERIE_NEWS_SAISONS[0]) : # Derniers épisodes Séries-TV ajoutée
                # surl  title 
                sTitle = aEntry[1]
                VSlog('SERIE_NEWS_SAISONS[0]='+sTitle) 
                
            elif (sUrl == SERIE_NEWS_EPISODES[0]) :
                ##url title lang
                sTitle = aEntry[1]
                sLang =aEntry[2]
                'Nouveaux épisodes ajoutés '
                VSlog('SERIE_NEWS_EPISODES[0]'+sTitle)
            
            elif ( '/films' in sUrl ) :##url image title quality lang
                sTitle = aEntry[2]
                sThumb = aEntry[1]
                sLang = aEntry[4]
                sQuality = aEntry[3]
                
            elif ( '/series' in sUrl ) :  #url image title    
                sThumb = aEntry[1]
                sTitle = aEntry[2]
                        
            else:
                #url     image   short title
                sTitle = aEntry[2]
            
            if not URL_MAIN in sThumb:
                sThumb = URL_MAIN +sThumb
            sDisplayTitle = ('%s (%s)(%s)') % (sTitle, sLang.upper(),sQuality.upper())
            
            
            VSlog('---------------------------------------------------')
            VSlog('ParameterHandler : ')
            VSlog('sThumb =  ' + sThumb)
            VSlog('description =  ' + sDesc)
            VSlog('sLang  = ' + sLang)
            VSlog('sQuality =  ' + sQuality)
            VSlog('sQuality =  ' + str(sTag))
            
               
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sLang ',  sLang )
            oOutputParameterHandler.addParameter('sQuality', sQuality)
            oOutputParameterHandler.addParameter('sTag', sTag)
            VSlog('ADD')
            
            if '/series' in sUrl and sUrl!= SERIE_NEWS_EPISODES[0] and sUrl!= SERIE_NEWS_SAISONS[0]: #showSaisons
                VSlog('CALL SHOW SAISONS'+sTitle)
                oGui.addTV(SITE_IDENTIFIER, 'showSaisons', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
            elif sUrl== SERIE_NEWS_SAISONS[0] :
                VSlog('CALL SHOW EPISODE +sTitle')
                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
            
            else:
                VSlog('CALL showHosters film ou news episodes ' +sTitle)
                oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
                
                     
        #progress_.VSclose(progress_)

        sNextPage = __checkForNextPage(sUrl, sHtmlContent)
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            number = re.search('/([0-9]+)', sNextPage).group(1)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Page ' + number + ' >>>[/COLOR]', oOutputParameterHandler)
    
    
    if not sSearch:  # Le moteur de recherche du site est correct, laisser le nextPage même en globalSearch
        oGui.setEndOfDirectory()


def __checkForNextPage(sUrl, sHtmlContent):
    # Récuperation de la page actuel dans l'url
    try:
        pageNext = int(re.search('page/([0-9]+)', sUrl).group(1)) + 1
    except AttributeError:
        pageNext = 2

    try:
        extractPageList = re.search('<div class="navigation">(.+?)</div>', sHtmlContent, re.MULTILINE | re.DOTALL).group(1)

        oParser = cParser()
        sPattern = '<a href="([^"]+)">' + str(pageNext) + '</a>'
        aResult = oParser.parse(extractPageList, sPattern)

        if (aResult[0] == True):
            nextPage = aResult[1][0]
            if not nextPage.startswith('https'):
                nextPage = URL_MAIN[:-1] + nextPage
            return nextPage
        return False

    except AttributeError:
        return False


#########################################################################




def showSaisons():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sTag= oInputParameterHandler.getValue('sTag')
    
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    VSlog('########  showEpisodes() '+sUrl)
    VSlog('########  stag '+str(sTag))
    
    oParser = cParser()
    sPattern='<div class="fsynopsis"><p>([^<]*)'
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        VSlog('description = true')
        sDesc = str(aResult[1][0])
        if (sTag != False):#\r\n\r\n'
            sDesc=sTag +'\r\n'+sDesc

   
    sPattern = 'images radius.+?ref="([^"]*)".+?src=".([^"]*).+?alt="([^"]*)' ## spat01
    #url     image   title
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
        for aEntry in aResult[1]:
        #for aEntry in reversed(aResult[1]): 
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sUrl2 = aEntry[0]
            sTitle = sMovieTitle + ' ' + aEntry[2]
            sThumb= URL_MAIN+aEntry[1]
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()

def showEpisodes():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sTag = oInputParameterHandler.getValue('sTag')

    VSlog('########  showEpisodes() '+sUrl)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    
    if (sDesc == '') :
        VSlog('description = rien '+ str(sDesc ))
    else :
        VSlog('description = qqles '+ str(sDesc ))
        
    #<div class="fsynopsis"><p>([^<]*)|saison([^<]*):<\/span>|href=".([^<]*)<span>.pisode([^<]*)
    #c'est tjrs les deux rectifier
    VSlog('description = ' + str(sDesc))
    #if (sDesc == '') :
    if (True) :   
        oParser = cParser()
        sPattern='<div class="fsynopsis"><p>([^<]*)'
        
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            VSlog('description = true')
            sDesc = str(aResult[1][0])
            if (sTag != False):#\r\n\r\n'
                sDesc=sTag +'\r\n'+sDesc
        
    #if (sThumb == ''):
    VSlog('thumb = ' + str(sDesc))
    if (True):  
        oParser = cParser()
        sPattern='og:image" content="([^"]*)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True): 
            sThumb =str( aResult[1][0])
            VSlog('thumb = true' + sThumb )
    
    sPattern = 'href=".([^<]*)<span>.pisode([^<]*)'
    sPattern = 'class="sais.+?href=".([^"]*).+?pisode([^<]*)'
    #match      href="([^"]*).>([^"]*)<span class="total
    
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        VSlog('aResult[0] == True)')   
        
        #for aEntry in aResult[1]:
        for aEntry in reversed(aResult[1]): 
            sUrl = URL_MAIN +  aEntry[0]
            sNumEp=str(aEntry[1]).replace(' ', '')
            sTitle =  sMovieTitle +' E' + sNumEp

            VSlog('ADD ' + sUrl  )
            VSlog('ADD ' + sMovieTitle )
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            #oGui.addEpisode(SITE_IDENTIFIER, 'seriesHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
    oGui.setEndOfDirectory()

def showHosters():
    
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sYear = oInputParameterHandler.getValue('sYear')
    sTag = oInputParameterHandler.getValue('sTag')
    
    
    
    VSlog('#### def showHosters()')
    VSlog('####           sUrl = ' + sUrl )
    
    
    oRequestHandler = cRequestHandler(sUrl.replace(' ', '%20'))
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    sHtmlContent = oRequestHandler.request()

    oParser = cParser()
    sPattern='<div class="fsynopsis"><p>([^<]*)'   
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        VSlog('description = true')
        sDesc = str(aResult[1][0])
        if ( sTag != False  and sTag != 'Langue' and sTag!='Qualité'   ):#\r\n\r\n'
            sDesc=sTag +'\r\n'+sDesc




    oParser = cParser()

    sPattern = 'data-num="([^"]*).+?data-code="([^"]*)".+?server player-([^"]*)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sHoster  = aEntry[2]
            data_num = aEntry[0]
            data_code = aEntry[1]
            sUrl2='https://wvw.filmgratuit.net/streamer.php?p=' + data_num + '&c=' + data_code
            #player.php
            #sTitle = ('%s [COLOR coral]%s[/COLOR]') % (sMovieTitle, sHoster)
            sDisplayTitle = ('%s (%s) [COLOR coral]%s[/COLOR]') % (sMovieTitle, 'sLang', sHoster)
            sDisplayTitle = ('%s  [COLOR coral]%s[/COLOR]') % (sMovieTitle, sHoster)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sUrlreferer', sUrl)
            
            #oGui.addMovie(SITE_IDENTIFIER, 'hostersLink', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
            oGui.addLink(SITE_IDENTIFIER, 'hostersLink', sDisplayTitle, sThumb, sDesc, oOutputParameterHandler)
           
        progress_.VSclose(progress_)


    oGui.setEndOfDirectory()


def hostersLink():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sUrlref = oInputParameterHandler.getValue('sUrlreferer')
   
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('Referer', sUrlref) 
    oRequestHandler.addHeaderEntry('User-Agent', ' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0')               
    oRequestHandler.request()
    sHosterUrl = oRequestHandler.getRealUrl()
   
    #sHosterUrl='https://uptostream.com/iframe/cawvv8v9rwo1'
    
    oHoster = cHosterGui().checkHoster(sHosterUrl) 
    if (oHoster != False):
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
 
    oGui.setEndOfDirectory()


