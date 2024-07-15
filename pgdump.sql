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
-- Name: VK_Favorit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."VK_Favorit" (
    id_user_vk integer NOT NULL,
    id_favorit_vk integer NOT NULL
);


ALTER TABLE public."VK_Favorit" OWNER TO postgres;

--
-- Name: favorits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.favorits (
    id_favorit integer NOT NULL,
    id_favorit_vk integer NOT NULL
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
-- Name: vk_id; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vk_id (
    id_user integer NOT NULL,
    id_user_vk bigint NOT NULL
);


ALTER TABLE public.vk_id OWNER TO postgres;

--
-- Name: vk_id_id_user_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vk_id_id_user_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vk_id_id_user_seq OWNER TO postgres;

--
-- Name: vk_id_id_user_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vk_id_id_user_seq OWNED BY public.vk_id.id_user;


--
-- Name: favorits id_favorit; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.favorits ALTER COLUMN id_favorit SET DEFAULT nextval('public.favorits_id_favorit_seq'::regclass);


--
-- Name: vk_id id_user; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vk_id ALTER COLUMN id_user SET DEFAULT nextval('public.vk_id_id_user_seq'::regclass);


--
-- Data for Name: VK_Favorit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."VK_Favorit" (id_user_vk, id_favorit_vk) FROM stdin;
\.


--
-- Data for Name: favorits; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.favorits (id_favorit, id_favorit_vk) FROM stdin;
\.


--
-- Data for Name: vk_id; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vk_id (id_user, id_user_vk) FROM stdin;
\.


--
-- Name: favorits_id_favorit_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.favorits_id_favorit_seq', 1, false);


--
-- Name: vk_id_id_user_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vk_id_id_user_seq', 1, false);


--
-- Name: VK_Favorit VK_Favorit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VK_Favorit"
    ADD CONSTRAINT "VK_Favorit_pkey" PRIMARY KEY (id_user_vk, id_favorit_vk);


--
-- Name: favorits favorits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.favorits
    ADD CONSTRAINT favorits_pkey PRIMARY KEY (id_favorit);


--
-- Name: vk_id vk_id_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vk_id
    ADD CONSTRAINT vk_id_pkey PRIMARY KEY (id_user);


--
-- Name: VK_Favorit VK_Favorit_id_favorit_vk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VK_Favorit"
    ADD CONSTRAINT "VK_Favorit_id_favorit_vk_fkey" FOREIGN KEY (id_favorit_vk) REFERENCES public.favorits(id_favorit);


--
-- Name: VK_Favorit VK_Favorit_id_user_vk_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VK_Favorit"
    ADD CONSTRAINT "VK_Favorit_id_user_vk_fkey" FOREIGN KEY (id_user_vk) REFERENCES public.vk_id(id_user);


--
-- PostgreSQL database dump complete
--

