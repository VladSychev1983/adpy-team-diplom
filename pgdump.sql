--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: TG_Favorit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."TG_Favorit" (
    id_tg_user integer NOT NULL,
    id_vk_user integer NOT NULL
);


ALTER TABLE public."TG_Favorit" OWNER TO postgres;

--
-- Name: favorits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.favorits (
    id_favorit integer NOT NULL,
    id_vk integer NOT NULL
);


ALTER TABLE public.favorits OWNER TO postgres;

--
-- Name: favorits_id_favorit_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.favorits_id_favorit_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.favorits_id_favorit_seq OWNER TO postgres;

--
-- Name: favorits_id_favorit_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.favorits_id_favorit_seq OWNED BY public.favorits.id_favorit;


--
-- Name: tg; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tg (
    id_tg integer NOT NULL,
    id_user_tg bigint NOT NULL
);


ALTER TABLE public.tg OWNER TO postgres;

--
-- Name: tg_id_tg_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tg_id_tg_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tg_id_tg_seq OWNER TO postgres;

--
-- Name: tg_id_tg_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tg_id_tg_seq OWNED BY public.tg.id_tg;


--
-- Name: favorits id_favorit; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.favorits ALTER COLUMN id_favorit SET DEFAULT nextval('public.favorits_id_favorit_seq'::regclass);


--
-- Name: tg id_tg; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tg ALTER COLUMN id_tg SET DEFAULT nextval('public.tg_id_tg_seq'::regclass);


--
-- Data for Name: TG_Favorit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."TG_Favorit" (id_tg_user, id_vk_user) FROM stdin;
\.


--
-- Data for Name: favorits; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.favorits (id_favorit, id_vk) FROM stdin;
\.


--
-- Data for Name: tg; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tg (id_tg, id_user_tg) FROM stdin;
\.


--
-- Name: favorits_id_favorit_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.favorits_id_favorit_seq', 1, false);


--
-- Name: tg_id_tg_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tg_id_tg_seq', 1, false);


--
-- Name: TG_Favorit TG_Favorit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TG_Favorit"
    ADD CONSTRAINT "TG_Favorit_pkey" PRIMARY KEY (id_tg_user, id_vk_user);


--
-- Name: favorits favorits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.favorits
    ADD CONSTRAINT favorits_pkey PRIMARY KEY (id_favorit);


--
-- Name: tg tg_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tg
    ADD CONSTRAINT tg_pkey PRIMARY KEY (id_tg);


--
-- Name: TG_Favorit TG_Favorit_id_tg_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TG_Favorit"
    ADD CONSTRAINT "TG_Favorit_id_tg_user_fkey" FOREIGN KEY (id_tg_user) REFERENCES public.tg(id_tg);


--
-- Name: TG_Favorit TG_Favorit_id_vk_user_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TG_Favorit"
    ADD CONSTRAINT "TG_Favorit_id_vk_user_fkey" FOREIGN KEY (id_vk_user) REFERENCES public.favorits(id_favorit);


--
-- PostgreSQL database dump complete
--

