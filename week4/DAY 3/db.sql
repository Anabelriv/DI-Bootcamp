toc.dat                                                                                             0000600 0004000 0002000 00000040507 14462666143 0014461 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP           ;                {        	   Hollywood    14.8 (Homebrew)    15.3 ;    R           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         S           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         T           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         U           1262    16402 	   Hollywood    DATABASE     m   CREATE DATABASE "Hollywood" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';
    DROP DATABASE "Hollywood";
                anabelrivera    false                     2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                anabelrivera    false         V           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   anabelrivera    false    4         �            1259    16404    actors    TABLE     �   CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(100) NOT NULL,
    age date NOT NULL,
    number_oscars smallint NOT NULL,
    city_id smallint
);
    DROP TABLE public.actors;
       public         heap    anabelrivera    false    4         �            1259    16403    actors_actor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.actors_actor_id_seq;
       public          anabelrivera    false    4    210         W           0    0    actors_actor_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.actor_id;
          public          anabelrivera    false    209         �            1259    16464    actors_movies    TABLE     l   CREATE TABLE public.actors_movies (
    id integer NOT NULL,
    actor_id integer,
    movie_id smallint
);
 !   DROP TABLE public.actors_movies;
       public         heap    anabelrivera    false    4         �            1259    16463    actors_movies_id_seq    SEQUENCE     �   CREATE SEQUENCE public.actors_movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.actors_movies_id_seq;
       public          anabelrivera    false    4    216         X           0    0    actors_movies_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.actors_movies_id_seq OWNED BY public.actors_movies.id;
          public          anabelrivera    false    215         �            1259    16417    country    TABLE     �   CREATE TABLE public.country (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    country_code smallint NOT NULL,
    CONSTRAINT country_country_code_check CHECK ((country_code < 50))
);
    DROP TABLE public.country;
       public         heap    anabelrivera    false    4         �            1259    16416    country_id_seq    SEQUENCE     �   CREATE SEQUENCE public.country_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.country_id_seq;
       public          anabelrivera    false    212    4         Y           0    0    country_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.country_id_seq OWNED BY public.country.id;
          public          anabelrivera    false    211         �            1259    16842    firsttab    TABLE     Q   CREATE TABLE public.firsttab (
    id integer,
    name character varying(10)
);
    DROP TABLE public.firsttab;
       public         heap    anabelrivera    false    4         �            1259    16452    movie    TABLE     z   CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying(50) NOT NULL,
    country_id smallint
);
    DROP TABLE public.movie;
       public         heap    anabelrivera    false    4         �            1259    16451    movie_id_seq    SEQUENCE     �   CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.movie_id_seq;
       public          anabelrivera    false    4    214         Z           0    0    movie_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;
          public          anabelrivera    false    213         �            1259    16512    movies_producers    TABLE     {   CREATE TABLE public.movies_producers (
    id integer NOT NULL,
    producer_id integer NOT NULL,
    movie_id smallint
);
 $   DROP TABLE public.movies_producers;
       public         heap    anabelrivera    false    4         �            1259    16511    movies_producers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_producers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.movies_producers_id_seq;
       public          anabelrivera    false    4    220         [           0    0    movies_producers_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.movies_producers_id_seq OWNED BY public.movies_producers.id;
          public          anabelrivera    false    219         �            1259    16493 	   producers    TABLE     �   CREATE TABLE public.producers (
    id integer NOT NULL,
    prod_name character varying(50) NOT NULL,
    country_id smallint
);
    DROP TABLE public.producers;
       public         heap    anabelrivera    false    4         �            1259    16492    producers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.producers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.producers_id_seq;
       public          anabelrivera    false    4    218         \           0    0    producers_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.producers_id_seq OWNED BY public.producers.id;
          public          anabelrivera    false    217         �            1259    16845 	   secondtab    TABLE     2   CREATE TABLE public.secondtab (
    id integer
);
    DROP TABLE public.secondtab;
       public         heap    anabelrivera    false    4         �           2604    16407    actors actor_id    DEFAULT     r   ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);
 >   ALTER TABLE public.actors ALTER COLUMN actor_id DROP DEFAULT;
       public          anabelrivera    false    209    210    210         �           2604    16467    actors_movies id    DEFAULT     t   ALTER TABLE ONLY public.actors_movies ALTER COLUMN id SET DEFAULT nextval('public.actors_movies_id_seq'::regclass);
 ?   ALTER TABLE public.actors_movies ALTER COLUMN id DROP DEFAULT;
       public          anabelrivera    false    215    216    216         �           2604    16420 
   country id    DEFAULT     h   ALTER TABLE ONLY public.country ALTER COLUMN id SET DEFAULT nextval('public.country_id_seq'::regclass);
 9   ALTER TABLE public.country ALTER COLUMN id DROP DEFAULT;
       public          anabelrivera    false    212    211    212         �           2604    16455    movie id    DEFAULT     d   ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);
 7   ALTER TABLE public.movie ALTER COLUMN id DROP DEFAULT;
       public          anabelrivera    false    213    214    214         �           2604    16515    movies_producers id    DEFAULT     z   ALTER TABLE ONLY public.movies_producers ALTER COLUMN id SET DEFAULT nextval('public.movies_producers_id_seq'::regclass);
 B   ALTER TABLE public.movies_producers ALTER COLUMN id DROP DEFAULT;
       public          anabelrivera    false    220    219    220         �           2604    16496    producers id    DEFAULT     l   ALTER TABLE ONLY public.producers ALTER COLUMN id SET DEFAULT nextval('public.producers_id_seq'::regclass);
 ;   ALTER TABLE public.producers ALTER COLUMN id DROP DEFAULT;
       public          anabelrivera    false    218    217    218         C          0    16404    actors 
   TABLE DATA           ^   COPY public.actors (actor_id, first_name, last_name, age, number_oscars, city_id) FROM stdin;
    public          anabelrivera    false    210       3651.dat I          0    16464    actors_movies 
   TABLE DATA           ?   COPY public.actors_movies (id, actor_id, movie_id) FROM stdin;
    public          anabelrivera    false    216       3657.dat E          0    16417    country 
   TABLE DATA           9   COPY public.country (id, name, country_code) FROM stdin;
    public          anabelrivera    false    212       3653.dat N          0    16842    firsttab 
   TABLE DATA           ,   COPY public.firsttab (id, name) FROM stdin;
    public          anabelrivera    false    221       3662.dat G          0    16452    movie 
   TABLE DATA           6   COPY public.movie (id, title, country_id) FROM stdin;
    public          anabelrivera    false    214       3655.dat M          0    16512    movies_producers 
   TABLE DATA           E   COPY public.movies_producers (id, producer_id, movie_id) FROM stdin;
    public          anabelrivera    false    220       3661.dat K          0    16493 	   producers 
   TABLE DATA           >   COPY public.producers (id, prod_name, country_id) FROM stdin;
    public          anabelrivera    false    218       3659.dat O          0    16845 	   secondtab 
   TABLE DATA           '   COPY public.secondtab (id) FROM stdin;
    public          anabelrivera    false    222       3663.dat ]           0    0    actors_actor_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.actors_actor_id_seq', 14, true);
          public          anabelrivera    false    209         ^           0    0    actors_movies_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.actors_movies_id_seq', 1, false);
          public          anabelrivera    false    215         _           0    0    country_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.country_id_seq', 4, true);
          public          anabelrivera    false    211         `           0    0    movie_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.movie_id_seq', 4, true);
          public          anabelrivera    false    213         a           0    0    movies_producers_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.movies_producers_id_seq', 8, true);
          public          anabelrivera    false    219         b           0    0    producers_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.producers_id_seq', 4, true);
          public          anabelrivera    false    217         �           2606    16469     actors_movies actors_movies_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.actors_movies DROP CONSTRAINT actors_movies_pkey;
       public            anabelrivera    false    216         �           2606    16409    actors actors_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (actor_id);
 <   ALTER TABLE ONLY public.actors DROP CONSTRAINT actors_pkey;
       public            anabelrivera    false    210         �           2606    16423    country country_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.country DROP CONSTRAINT country_pkey;
       public            anabelrivera    false    212         �           2606    16457    movie movie_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.movie DROP CONSTRAINT movie_pkey;
       public            anabelrivera    false    214         �           2606    16517 &   movies_producers movies_producers_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.movies_producers
    ADD CONSTRAINT movies_producers_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.movies_producers DROP CONSTRAINT movies_producers_pkey;
       public            anabelrivera    false    220         �           2606    16498    producers producers_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.producers
    ADD CONSTRAINT producers_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.producers DROP CONSTRAINT producers_pkey;
       public            anabelrivera    false    218         �           2606    16426    actors actors_city_id_fkey    FK CONSTRAINT     {   ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.country(id);
 D   ALTER TABLE ONLY public.actors DROP CONSTRAINT actors_city_id_fkey;
       public          anabelrivera    false    210    212    3495         �           2606    16470 )   actors_movies actors_movies_actor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(actor_id);
 S   ALTER TABLE ONLY public.actors_movies DROP CONSTRAINT actors_movies_actor_id_fkey;
       public          anabelrivera    false    210    3493    216         �           2606    16475 )   actors_movies actors_movies_movie_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);
 S   ALTER TABLE ONLY public.actors_movies DROP CONSTRAINT actors_movies_movie_id_fkey;
       public          anabelrivera    false    214    216    3497         �           2606    16458    movie movie_country_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(id);
 E   ALTER TABLE ONLY public.movie DROP CONSTRAINT movie_country_id_fkey;
       public          anabelrivera    false    214    3495    212         �           2606    16523 /   movies_producers movies_producers_movie_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.movies_producers
    ADD CONSTRAINT movies_producers_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);
 Y   ALTER TABLE ONLY public.movies_producers DROP CONSTRAINT movies_producers_movie_id_fkey;
       public          anabelrivera    false    214    220    3497         �           2606    16518 2   movies_producers movies_producers_producer_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.movies_producers
    ADD CONSTRAINT movies_producers_producer_id_fkey FOREIGN KEY (producer_id) REFERENCES public.producers(id);
 \   ALTER TABLE ONLY public.movies_producers DROP CONSTRAINT movies_producers_producer_id_fkey;
       public          anabelrivera    false    218    220    3501         �           2606    16499 #   producers producers_country_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.producers
    ADD CONSTRAINT producers_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(id);
 M   ALTER TABLE ONLY public.producers DROP CONSTRAINT producers_country_id_fkey;
       public          anabelrivera    false    212    218    3495                                                                                                                                                                                                 3651.dat                                                                                            0000600 0004000 0002000 00000000611 14462666143 0014262 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        7	Patrick	Jolie	1980-04-22	1	\N
8	Marc	Benichou	1998-11-02	0	\N
10	Lea	Benichou	1987-07-27	0	\N
1	Matt	Damon	1970-08-10	5	2
3	Matt	Damon	1970-08-10	5	2
6	Matt	Damon	1982-11-22	2	2
2	George	Clooney	1961-06-05	2	2
4	George	Clooney	1961-06-05	2	2
11	Amelia	Dux	1996-04-07	0	3
12	David	Grez	2003-06-14	0	3
5	Brad	Pitt	1980-04-22	1	4
9	Yoan	Cohen	2010-12-03	0	4
13	Omer	Simpson	1980-10-03	1	4
\.


                                                                                                                       3657.dat                                                                                            0000600 0004000 0002000 00000000005 14462666143 0014265 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3653.dat                                                                                            0000600 0004000 0002000 00000000047 14462666143 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2	USA	40
3	France	33
4	Britain	20
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         3662.dat                                                                                            0000600 0004000 0002000 00000000051 14462666143 0014262 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        5	Pawan
6	Sharlee
7	Krish
\N	Avtaar
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       3655.dat                                                                                            0000600 0004000 0002000 00000000113 14462666143 0014263 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Good Will Hunting	2
2	Jason Bourne	2
3	Oceans Twelve	4
4	Oceans 8	4
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                     3661.dat                                                                                            0000600 0004000 0002000 00000000043 14462666143 0014262 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        4	1	1
5	3	2
6	4	3
7	2	4
8	1	4
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             3659.dat                                                                                            0000600 0004000 0002000 00000000104 14462666143 0014267 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Jane Dow	2
2	James Smith	2
3	Ben Thompson	4
4	Daniel Alves	4
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                            3663.dat                                                                                            0000600 0004000 0002000 00000000012 14462666143 0014260 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        5
\N
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      restore.sql                                                                                         0000600 0004000 0002000 00000032055 14462666143 0015405 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 14.8 (Homebrew)
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE "Hollywood";
--
-- Name: Hollywood; Type: DATABASE; Schema: -; Owner: anabelrivera
--

CREATE DATABASE "Hollywood" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'C';


ALTER DATABASE "Hollywood" OWNER TO anabelrivera;

\connect "Hollywood"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: anabelrivera
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO anabelrivera;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(100) NOT NULL,
    age date NOT NULL,
    number_oscars smallint NOT NULL,
    city_id smallint
);


ALTER TABLE public.actors OWNER TO anabelrivera;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: anabelrivera
--

CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_actor_id_seq OWNER TO anabelrivera;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anabelrivera
--

ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.actor_id;


--
-- Name: actors_movies; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.actors_movies (
    id integer NOT NULL,
    actor_id integer,
    movie_id smallint
);


ALTER TABLE public.actors_movies OWNER TO anabelrivera;

--
-- Name: actors_movies_id_seq; Type: SEQUENCE; Schema: public; Owner: anabelrivera
--

CREATE SEQUENCE public.actors_movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_movies_id_seq OWNER TO anabelrivera;

--
-- Name: actors_movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anabelrivera
--

ALTER SEQUENCE public.actors_movies_id_seq OWNED BY public.actors_movies.id;


--
-- Name: country; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.country (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    country_code smallint NOT NULL,
    CONSTRAINT country_country_code_check CHECK ((country_code < 50))
);


ALTER TABLE public.country OWNER TO anabelrivera;

--
-- Name: country_id_seq; Type: SEQUENCE; Schema: public; Owner: anabelrivera
--

CREATE SEQUENCE public.country_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.country_id_seq OWNER TO anabelrivera;

--
-- Name: country_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anabelrivera
--

ALTER SEQUENCE public.country_id_seq OWNED BY public.country.id;


--
-- Name: firsttab; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.firsttab (
    id integer,
    name character varying(10)
);


ALTER TABLE public.firsttab OWNER TO anabelrivera;

--
-- Name: movie; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying(50) NOT NULL,
    country_id smallint
);


ALTER TABLE public.movie OWNER TO anabelrivera;

--
-- Name: movie_id_seq; Type: SEQUENCE; Schema: public; Owner: anabelrivera
--

CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movie_id_seq OWNER TO anabelrivera;

--
-- Name: movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anabelrivera
--

ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;


--
-- Name: movies_producers; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.movies_producers (
    id integer NOT NULL,
    producer_id integer NOT NULL,
    movie_id smallint
);


ALTER TABLE public.movies_producers OWNER TO anabelrivera;

--
-- Name: movies_producers_id_seq; Type: SEQUENCE; Schema: public; Owner: anabelrivera
--

CREATE SEQUENCE public.movies_producers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_producers_id_seq OWNER TO anabelrivera;

--
-- Name: movies_producers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anabelrivera
--

ALTER SEQUENCE public.movies_producers_id_seq OWNED BY public.movies_producers.id;


--
-- Name: producers; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.producers (
    id integer NOT NULL,
    prod_name character varying(50) NOT NULL,
    country_id smallint
);


ALTER TABLE public.producers OWNER TO anabelrivera;

--
-- Name: producers_id_seq; Type: SEQUENCE; Schema: public; Owner: anabelrivera
--

CREATE SEQUENCE public.producers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.producers_id_seq OWNER TO anabelrivera;

--
-- Name: producers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: anabelrivera
--

ALTER SEQUENCE public.producers_id_seq OWNED BY public.producers.id;


--
-- Name: secondtab; Type: TABLE; Schema: public; Owner: anabelrivera
--

CREATE TABLE public.secondtab (
    id integer
);


ALTER TABLE public.secondtab OWNER TO anabelrivera;

--
-- Name: actors actor_id; Type: DEFAULT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);


--
-- Name: actors_movies id; Type: DEFAULT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors_movies ALTER COLUMN id SET DEFAULT nextval('public.actors_movies_id_seq'::regclass);


--
-- Name: country id; Type: DEFAULT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.country ALTER COLUMN id SET DEFAULT nextval('public.country_id_seq'::regclass);


--
-- Name: movie id; Type: DEFAULT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);


--
-- Name: movies_producers id; Type: DEFAULT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movies_producers ALTER COLUMN id SET DEFAULT nextval('public.movies_producers_id_seq'::regclass);


--
-- Name: producers id; Type: DEFAULT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.producers ALTER COLUMN id SET DEFAULT nextval('public.producers_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.actors (actor_id, first_name, last_name, age, number_oscars, city_id) FROM stdin;
\.
COPY public.actors (actor_id, first_name, last_name, age, number_oscars, city_id) FROM '$$PATH$$/3651.dat';

--
-- Data for Name: actors_movies; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.actors_movies (id, actor_id, movie_id) FROM stdin;
\.
COPY public.actors_movies (id, actor_id, movie_id) FROM '$$PATH$$/3657.dat';

--
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.country (id, name, country_code) FROM stdin;
\.
COPY public.country (id, name, country_code) FROM '$$PATH$$/3653.dat';

--
-- Data for Name: firsttab; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.firsttab (id, name) FROM stdin;
\.
COPY public.firsttab (id, name) FROM '$$PATH$$/3662.dat';

--
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.movie (id, title, country_id) FROM stdin;
\.
COPY public.movie (id, title, country_id) FROM '$$PATH$$/3655.dat';

--
-- Data for Name: movies_producers; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.movies_producers (id, producer_id, movie_id) FROM stdin;
\.
COPY public.movies_producers (id, producer_id, movie_id) FROM '$$PATH$$/3661.dat';

--
-- Data for Name: producers; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.producers (id, prod_name, country_id) FROM stdin;
\.
COPY public.producers (id, prod_name, country_id) FROM '$$PATH$$/3659.dat';

--
-- Data for Name: secondtab; Type: TABLE DATA; Schema: public; Owner: anabelrivera
--

COPY public.secondtab (id) FROM stdin;
\.
COPY public.secondtab (id) FROM '$$PATH$$/3663.dat';

--
-- Name: actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anabelrivera
--

SELECT pg_catalog.setval('public.actors_actor_id_seq', 14, true);


--
-- Name: actors_movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anabelrivera
--

SELECT pg_catalog.setval('public.actors_movies_id_seq', 1, false);


--
-- Name: country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anabelrivera
--

SELECT pg_catalog.setval('public.country_id_seq', 4, true);


--
-- Name: movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anabelrivera
--

SELECT pg_catalog.setval('public.movie_id_seq', 4, true);


--
-- Name: movies_producers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anabelrivera
--

SELECT pg_catalog.setval('public.movies_producers_id_seq', 8, true);


--
-- Name: producers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: anabelrivera
--

SELECT pg_catalog.setval('public.producers_id_seq', 4, true);


--
-- Name: actors_movies actors_movies_pkey; Type: CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_pkey PRIMARY KEY (id);


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (actor_id);


--
-- Name: country country_pkey; Type: CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT country_pkey PRIMARY KEY (id);


--
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


--
-- Name: movies_producers movies_producers_pkey; Type: CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movies_producers
    ADD CONSTRAINT movies_producers_pkey PRIMARY KEY (id);


--
-- Name: producers producers_pkey; Type: CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.producers
    ADD CONSTRAINT producers_pkey PRIMARY KEY (id);


--
-- Name: actors actors_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.country(id);


--
-- Name: actors_movies actors_movies_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(actor_id);


--
-- Name: actors_movies actors_movies_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);


--
-- Name: movie movie_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(id);


--
-- Name: movies_producers movies_producers_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movies_producers
    ADD CONSTRAINT movies_producers_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movie(id);


--
-- Name: movies_producers movies_producers_producer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.movies_producers
    ADD CONSTRAINT movies_producers_producer_id_fkey FOREIGN KEY (producer_id) REFERENCES public.producers(id);


--
-- Name: producers producers_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: anabelrivera
--

ALTER TABLE ONLY public.producers
    ADD CONSTRAINT producers_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.country(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: anabelrivera
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   